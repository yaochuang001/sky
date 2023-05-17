from django.shortcuts import render
from django.http import JsonResponse
from sky import models as sky_models
from django.db.models.functions import ExtractMonth
from django.db.models import Sum
from rjd import models
import datetime
# 转化成字典
from django.forms.models import model_to_dict

from sky.utils import data_date
from django.views.decorators.csrf import csrf_exempt


def inventory_chart(request):
    """盘点统计"""
    now_time = datetime.datetime.now()
    search_year = request.GET.get('year', '')
    if not search_year:
        search_year = now_time.year
    context = {
        'search_year': search_year
    }
    return render(request, 'inventory_chart.html', context)


@csrf_exempt
def inventory_chart_bar(request):
    """构造柱状图产量数据"""
    year = request.POST.get('year')
    pub_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pri_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pub = models.PublicAccount.objects.annotate(month=ExtractMonth('create_time')). \
        values('month').annotate(zonghe=Sum('total_price')).filter(create_time__year=year)
    for item in pub:
        pub_data[item['month'] - 1] = item['zonghe']
    pri = models.PrivateAccount.objects.annotate(month=ExtractMonth('create_time')). \
        values('month').annotate(zonghe=Sum('total_price')).filter(create_time__year=year)
    for item in pri:
        pri_data[item['month'] - 1] = item['zonghe']
    legend = ['对公总账', '对私总账']
    series_list = [
        {
            "name": '对公总账',
            "type": 'bar',
            "data": pub_data,
        },
        {
            "name": '对私总账',
            "type": 'bar',
            "data": pri_data,
        },
    ]
    x_axis = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']
    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)


@csrf_exempt
def inventory_status(request):
    """构造运行数据"""
    result = {}
    result['rjd_cash'] = 80000
    try:
        now_time = datetime.datetime.now()
        year = request.POST.get('year')
        year_last = str(int(year) - 1)
        pub_total = 0
        pri_total = 0
        pub_last_total = 0
        pri_last_total = 0
        pub = models.PublicAccount.objects.filter(create_time__year=year) \
            .aggregate(total=Sum('total_price'))
        pri = models.PrivateAccount.objects.filter(create_time__year=year) \
            .aggregate(total=Sum('total_price'))
        pub_last = models.PublicAccount.objects.filter(create_time__year=year_last) \
            .aggregate(total=Sum('total_price'))
        pri_last = models.PrivateAccount.objects.filter(create_time__year=year_last) \
            .aggregate(total=Sum('total_price'))
        if pub['total']:
            pub_total = pub['total']
        if pri['total']:
            pri_total = pri['total']
        result['year_cost'] = pub_total + pri_total
        if pub_last['total']:
            pub_last_total = pub_last['total']
        if pri_last['total']:
            pri_last_total = pri_last['total']
        result['last_year_cost'] = pub_last_total + pri_last_total
        rjd_unpaid = models.Unpaid.objects.aggregate(total=Sum('final_payment'))
        result['rjd_unpaid'] = rjd_unpaid['total']
        rjd_final_payment = models.AccountsReceivable.objects.aggregate(total=Sum('final_payment'))
        result['rjd_final_payment'] = rjd_final_payment['total']
        result['status'] = True
    except Exception as e:
        result['status'] = False
    print(result)
    return JsonResponse(result)

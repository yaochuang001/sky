from django.shortcuts import render, redirect
from rjd.form.form import *
from app_cw.utils.pagination import Pagination
import datetime


def account_pri_list(request):
    """对私报表"""
    now_time = datetime.datetime.now()
    data_dict = {}
    # 数据收集
    search_data = request.GET.get('q', "")
    search_date = request.GET.get('d', '')
    search_date2 = request.GET.get('d2', '')
    if search_date:
        start_date = datetime.date(*map(int, search_date.split('-')))
    else:
        start_date = ''
    if search_date2:
        end_date = datetime.date(*map(int, search_date2.split('-')))
    else:
        end_date = ''
    if search_data:
        data_dict["supplier__supplier_name__contains"] = search_data
    if start_date and end_date:
        queryset = models.PrivateAccount.objects.filter(**data_dict,
                                                        create_time__range=(start_date, end_date)).order_by('-id')
    else:
        queryset = models.PrivateAccount.objects.filter(**data_dict,create_time__year=now_time.year,
                                                        create_time__month=now_time.month).order_by('-id')

    page_object = Pagination(request, queryset)
    context = {
        'queryset': page_object.page_queryset,
        'search_data': search_data,
        'page_string': page_object.html(),
        'search_date': search_date,
        'search_date2': search_date2,
    }
    return render(request, 'account_pri_list.html', context)


def account_pri_add(request):
    """添加对私账单"""
    if request.method == "GET":
        form = AccountPriModelForm()
        context = {
            'form': form,
            'title': "添加对私付款",
        }
        return render(request, 'rjd_add.html', context)
    form = AccountPriModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/rjd/account/pri/list/')
    context = {
        'form': form,
        'title': "添加对私付款",
    }
    return render(request, 'rjd_add.html', context)


def account_pri_edit(request, nid):
    """编辑已付对私账单"""
    row_object = models.PrivateAccount.objects.filter(id=nid).first()

    if request.method == "GET":
        form = AccountPriModelForm(instance=row_object)
        context = {
            'form': form,
            'title': '编辑对私已付',
        }
        return render(request, 'rjd_add.html', context)
    form = AccountPriModelForm(data=request.POST, instance=row_object, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/rjd/account/pri/list/')
    context = {
        'form': form,
        'title': '编辑对私已付',
    }
    return render(request, 'rjd_add.html', context)


def account_pri_delete(request, nid):
    """删除单行对私账单"""
    models.PrivateAccount.objects.filter(id=nid).delete()
    return redirect('/rjd/account/pri/list/')

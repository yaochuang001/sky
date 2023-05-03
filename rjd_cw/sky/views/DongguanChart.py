from django.shortcuts import render
from django.http import JsonResponse
from sky import models
import datetime
# 转化成字典
from django.forms.models import model_to_dict
# 聚合函数
from django.db import connection, close_old_connections

from app_cw.utils.pagination import Pagination
from sky.utils import data_date
from django.views.decorators.csrf import csrf_exempt


def dg_chart(request):
    """东莞实时数据"""
    sql = "select * from sky_dgdata where id in(select max(id)from sky_dgdata group by name) order by name"
    queryset = models.DgData.objects.raw(sql)
    """

    for obj in queryset:
        print(obj.id,obj.name,obj.account,obj.create_time.strftime("%Y-%m-%d"),obj.gender,obj.get_gender_display(),obj.depart_id,obj.depart.title)

    """
    context = {
        "queryset": queryset,
    }
    return render(request, 'dg_chart.html', context)


def dg_chart_op(request):
    """获取东莞实时产量"""
    x_list = []
    data_list = []
    sql_op = "select name,op_everyday from sky_dgstatus where" \
             " id in(select max(id) id from sky_dgstatus group by name)order by name;"
    cursor = connection.cursor()
    cursor.execute(sql_op)
    ret = cursor.fetchall()
    for item in ret:
        x_list.append(item[0])
        data_list.append(item[1])
    """构造柱状图产量数据"""
    legend = ['单机产量']
    series_list = [
        {
            "name": '单机产量',
            "type": 'bar',
            "data": data_list
        },
    ]
    x_axis = x_list
    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)


def dg_chart_eff(request):
    """获取东莞实时节拍"""
    x_list = []
    data_list = []
    sql_op = "select name,efficiency_avg from sky_dgstatus where" \
             " id in(select max(id) id from sky_dgstatus group by name)order by name;"
    cursor = connection.cursor()
    cursor.execute(sql_op)
    ret = cursor.fetchall()
    for item in ret:
        x_list.append(item[0])
        data_list.append(item[1])

    legend = ['生产平均节拍']
    series_list = [
        {
            "name": '生产平均节拍',
            "type": 'bar',
            "data": data_list
        },

    ]
    x_axis = x_list
    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)


def dg_chart_kj(request):
    """构造开机数量"""
    sql_work = "select count(id) from sky_dgdata where id in(select max(id)" \
               " from sky_dgdata group by name) and sys_status =100"
    sql_stop = "select count(id) from sky_dgdata where id in(select max(id) " \
               "from sky_dgdata group by name) and sys_status =200"
    cursor = connection.cursor()
    cursor.execute(sql_work)
    work = cursor.fetchall()[0][0]
    cursor.execute(sql_stop)
    stop = cursor.fetchall()[0][0]

    series_list = [
        {
            "name": 'Access From',
            "type": 'pie',
            "radius": '50%',
            "data": [
                {"value": stop, "name": '停机数量'},
                {"value": work, "name": '运行数量'},

            ],
            "emphasis": {
                "itemStyle": {
                    "shadowBlur": 10,
                    "shadowOffsetX": 0,
                    "shadowColor": 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
    result = {
        "status": True,
        "data": {
            'series_list': series_list,
        }
    }
    return JsonResponse(result)


def dg_chart_self(request):
    """注塑机械手"""
    name = request.GET.get('name')
    context = {
        "equipment": name
    }

    return render(request, 'dg_chart_self.html', context)


@csrf_exempt
def dg_chart_self_op(request):
    """构造柱状图产量数据"""
    name = request.POST.get('name')
    day_output = data_date.get_week_dg_data(4, name)
    day_eff = data_date.get_lastweek_dg_data(4, name)
    legend = ['本周产量', '上周产量']
    series_list = [
        {
            "name": '本周产量',
            "type": 'bar',
            "data": [day_output['星期一'], day_output['星期二'], day_output['星期三'],
                     day_output['星期四'], day_output['星期五'], day_output['星期六'],
                     day_output['星期天'], ]
        },
        {
            "name": '上周产量',
            "type": 'bar',
            "data": [day_eff['星期一'], day_eff['星期二'], day_eff['星期三'],
                     day_eff['星期四'], day_eff['星期五'], day_eff['星期六'],
                     day_eff['星期天'], ]
        },
    ]
    x_axis = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
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
def dg_chart_self_eff(request):
    """构造曲线图开机率数据"""
    name = request.POST.get('name')
    work_pro = data_date.get_week_dg_data(2, name)  # 每天运行率
    work_list = []
    for item in work_pro:
        if item == '结果':
            continue
        work_list.append(round(work_pro[item] * 5 / 3600, 3))
    error_pro = data_date.get_week_dg_data(3, name)  # 每天报警率
    error_list = []
    for item in error_pro:
        if item == '结果':
            continue
        error_list.append(round(error_pro[item] * 5 / 3600, 3))
    date = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    result = {
        "status": True,
        "data": [work_list, error_list],
        "date": date,
    }
    return JsonResponse(result)


@csrf_exempt
def dg_chart_self_sta(request):
    """构造运行数据"""
    today = datetime.date.today()
    name = request.POST.get('name')
    try:
        res = models.DgData.objects.filter(c_time__year=today.year, c_time__month=today.month,
                                           c_time__day=today.day, name=name).latest('id')
        res_status = models.DgStatus.objects.filter(c_time__year=today.year, c_time__month=today.month,
                                                    c_time__day=today.day, name=name).latest('id')
        day_output = data_date.get_week_dg_data(4, name)#获取周总产量
        op_week = 0
        for day_op in day_output:
            if day_op == '结果':
                continue
            op_week = day_output[day_op]+op_week
        data = model_to_dict(res)
        status = model_to_dict(res_status)
        del status['id']
        del status['name']
        res_list = dict(data, **status)
        res_list['week_output'] = op_week
        for res in res_list:
            if res == 'sys_status':
                if res_list[res] == 100:
                    res_list[res] = "系统运行中"
                else:
                    res_list[res] = "系统停机中"
            if res == 'work':
                res_list[res] = round(res_list[res] * 5 / 3600, 3)
            if res == 'efficiency_avg':
                res_list[res] = round(res_list[res]/10, 1)
            if res == 'efficiency':
                res_list[res] = round(res_list[res]/10, 1)

    except Exception as e:
        res_list = {}
        res_list['错误'] = str(e)
    result = {
        "status": True,
        'res_list': res_list
    }
    return JsonResponse(result)

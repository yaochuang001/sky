from django.shortcuts import render
from django.http import JsonResponse
from sky import models
import datetime
# 转化成字典
from django.forms.models import model_to_dict

from app_cw.utils.pagination import Pagination
from sky.utils import data_date


def robot_chart(request):
    """注塑机械手"""
    # 获取所有的数据表
    queryset = models.RobotData.objects.all().order_by("-id")[:100]

    page_object = Pagination(request, queryset, page_size=30)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }

    return render(request, 'robot_chart.html', context)


def robot_char_bar(request):
    """构造柱状图产量数据"""
    day_output = data_date.get_week_data(9)  # 每天产量
    plane_output = data_date.get_last_week_data(9) # 上周产量
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
            "data": [plane_output['星期一'], plane_output['星期二'], plane_output['星期三'],
                     plane_output['星期四'], plane_output['星期五'], plane_output['星期六'],
                     plane_output['星期天'], ]
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


def robot_char_pie(request):
    """构造饼状图开机数据"""
    today = datetime.date.today()  # 当前日期
    row_object = models.RobotStatus.objects.filter(time=today).values("work", "stop", "test", "work_error").first()
    if row_object == None:
        work = '0'
        stop = '0'
        test = '0'
        work_error = '0'
    else:
        work = str(round(row_object['work']*5/3600,3))
        stop = str(round(row_object['stop']*5/3600,3))
        test = str(round(row_object['test']*5/3600,3))
        work_error = str(round(row_object['work_error']*5/3600,3))
    series_list = [
        {
            "name": 'Access From',
            "type": 'pie',
            "radius": '50%',
            "data": [
                {"value": work, "name": '运行时间'},
                {"value": stop, "name": '停机时间'},
                {"value": work_error, "name": '报警时间'},
                {"value": test, "name": '调机时间'},
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


def robot_char_line(request):
    """构造曲线图开机率数据"""
    work_pro= data_date.get_week_data(6)  # 每天运行率
    work_list = []
    for item in work_pro:
        if item == '结果':
            continue
        work_list.append((work_pro[item])*100)
    error_pro = data_date.get_week_data(7)  # 每天报警率
    error_list = []
    for item in error_pro:
        if item == '结果':
            continue
        error_list.append((error_pro[item])*100)
    date = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    result = {
        "status": True,
        "data": [work_list,error_list],
        "date": date,
    }
    return JsonResponse(result)


def robot_status(request):
    """构造运行数据"""
    try:
        today = datetime.date.today()
        res = models.RobotData.objects.filter(c_time__year=today.year, c_time__month=today.month,
                                              c_time__day=today.day).latest('id')
        res_list = model_to_dict(res)
        for res in res_list:
            if res == 'sys_status':
                if res_list[res] == 100:
                    res_list[res] = "系统运行中"
                elif res_list[res] == 200:
                    res_list[res] = "自动运行停止"
                elif res_list[res] == 300:
                    res_list[res] = "设备调机中"
                elif res_list[res] == 400:
                    res_list[res] = "设备报警"
                else:
                    res_list[res] = "系统未使能"
            elif res == 'work_status':
                if res_list[res] == 100:
                    res_list[res] = "开启自动程序"
                elif res_list[res] == 200:
                    res_list[res] = "开启复位程序"
                elif res_list[res] == 300:
                    res_list[res] = "手动控制中"
                else:
                    res_list[res] = "系统关机中"
            else:
                continue
    except Exception as e:
        res_list = {}
        res_list['错误'] = str(e)
    result = {
        "status": True,
        'res_list': res_list
    }
    return JsonResponse(result)

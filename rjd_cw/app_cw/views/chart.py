from django.shortcuts import render
from django.http import JsonResponse


def chart_list(request):
    """数据统计页面"""

    return render(request, 'chart_list.html')


def char_bar(request):
    """构造柱状数据"""
    legend = ['当月产量', '计划产量']
    series_list = [
        {
            "name": '当月产量',
            "type": 'bar',
            "data": [63456, 78567, 78666, 56890, 89087, 56789, 78654, 99965, 99687, 99786, 98676, 98765, ]
        },
        {
            "name": '计划产量',
            "type": 'bar',
            "data": [60000, 75000, 75000, 60000, 85000, 60000, 75000, 95000, 95000, 95000, 95000, 90000, ]
        },
    ]
    x_axis = ['2022-01', '2022-02', '2022-03', '2022-04', '2022-05', '2022-06', '2022-07', '2022-08', '2022-09',
              '2022-10', '2022-11', '2022-12']

    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)

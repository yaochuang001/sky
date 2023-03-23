from django.shortcuts import render
from django.http import JsonResponse

def chart_list(request):
    """数据统计页面"""

    return render(request, 'chart_list.html')


def char_bar(request):
    """构造柱状数据"""
    legend = ['荔枝','两千金']
    series_list = [
        {
            "name": '荔枝',
            "type": 'bar',
            "data": [12, 13, 44, 33, 22, 109]
        },
        {
            "name": '两千金',
            "type": 'bar',
            "data": [15, 23, 24, 23, 32, 19]
        },
    ]
    x_axis = ['1月','2月','3月','4月','5月','6月',]

    result = {
        "status":True,
        "data":{
            'legend':legend,
            'series_list':series_list,
            'x_axis':x_axis,
        }
    }
    return JsonResponse(result)

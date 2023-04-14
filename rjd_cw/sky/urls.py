from django.urls import path
from sky.views import LongHuaChart, RobotChart, DongguanChart

urlpatterns = [
    # 龙华注塑厂
    path('lh/chart/', LongHuaChart.lh_chart),
    path('lh/data/add', LongHuaChart.lh_data_add),

    # 注塑机械手
    path('robot/chart/', RobotChart.robot_chart),
    path('robot/chart/bar/', RobotChart.robot_char_bar),
    path('robot/chart/pie/', RobotChart.robot_char_pie),
    path('robot/chart/line/', RobotChart.robot_char_line),
    path('robot/status/', RobotChart.robot_status),

    # 东莞注塑厂
    path('dg/chart/', DongguanChart.dg_chart),
    path('dg/chart/op/', DongguanChart.dg_chart_op),
    path('dg/chart/eff/', DongguanChart.dg_chart_eff),
    path('dg/chart/kj/', DongguanChart.dg_chart_kj),
    path('dg/chart/self/', DongguanChart.dg_chart_self),
    path('dg/chart/self_op/', DongguanChart.dg_chart_self_op),
    path('dg/chart/self_eff/', DongguanChart.dg_chart_self_eff),
    path('dg/chart/self_sta/', DongguanChart.dg_chart_self_sta),

]

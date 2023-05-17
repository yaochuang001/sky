
$(function(){
    initBar();
    initStatus();
})

function initBar(){
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('m1'));
    // 指定图表的配置项和数据
    var option = {
        title: {
          text: '月度花费总和',
          textAlign:"auto",
          left:"center",
        },
        tooltip: {},
        legend: {
          data: [],
          bottom:0
        },
        xAxis: {
          data: []
        },
        yAxis: {},
        series: []
    };
    // 获取数据
    $.ajax({
        url:"/rjd/inventory/chart/bar/",
        type: 'post',
        data:$("#inventory_form").serialize(),
        dataType:"JSON",
        success:function(res){
            // 将后台返回的数据，更新到option中
            if(res.status){
                 option.legend.data = res.data.legend;
                 option.xAxis.data = res.data.x_axis;
                 option.series = res.data.series_list;
                // 使用刚指定的配置项和数据显示图表。
                myChart.setOption(option);
                window.addEventListener('resize', () => {
                    myChart.resize()
                });
            }
        }
    });
}
function initStatus(){
    // 获取数据
    $.ajax({
        url:'/rjd/inventory/status/',
        type: 'post',
        data:$("#inventory_form").serialize(),
        dataType:"JSON",
        success:function(res){
            // 将后台返回的数据，更新到option中
            if(res.status){
            $('#rjd_cash').text(res.rjd_cash);
            $('#rjd_unpaid').text(res.rjd_unpaid);
            $('#final_payment').text(res.rjd_final_payment);
            $('#year_cost').text(res.year_cost);
            $('#last_year_cost').text(res.last_year_cost);
        }else{
            console.log('接口错误')
        }
            }
    });

}

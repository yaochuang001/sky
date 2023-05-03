
$(function(){
    init_op();
    init_eff();
    init_kj();
    setInterval(init_op,60000);
    setInterval(init_eff,60000);
    setInterval(init_kj,60000);
})
function init_op(){
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('m2'));
    // 指定图表的配置项和数据
    var option = {
        title: {
          text: '当前产量',
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
        url:"/sky/dg/chart/op/",
        type:"get",
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
function init_eff(){
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('m1'));
    // 指定图表的配置项和数据
    var option = {
        title: {
          text: '平均节拍',
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
        url:"/sky/dg/chart/eff/",
        type:"get",
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
function init_kj(){
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('m3'));
    // 指定图表的配置项和数据
    var option = {
      title: {
        text: '运行效率',
        subtext: '开机率',
        left: 'center'
      },
      tooltip: {
        trigger: 'item'
      },
      legend: {
        bottom:0,
      },
      series: []
    };
        // 获取数据
    $.ajax({
        url:"/sky/dg/chart/kj/",
        type:"get",
        dataType:"JSON",
        success:function(res){
            // 将后台返回的数据，更新到option中
            if(res.status){
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


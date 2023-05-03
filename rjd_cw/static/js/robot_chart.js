
$(function(){
    initLine();
    initBar();
    initPie();
    initStatus();
    setInterval(initLine,1000);
    setInterval(initBar,1000);
    setInterval(initPie,1000);
    setInterval(initStatus,2000);
})

function initBar(){
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('m2'));
    // 指定图表的配置项和数据
    var option = {
        title: {
          text: '周产量',
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
        url:"/sky/robot/chart/bar/",
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
function initPie(){
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
        url:"/sky/robot/chart/pie/",
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
function initLine(){
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('m1'));

    // 指定图表的配置项和数据
    const colors = ['#5470C6', '#EE6666'];
    var option = {
          color: colors,
          tooltip: {
            trigger: 'none',
            axisPointer: {
              type: 'cross'
            }
          },
          legend: {},
            grid: {
                top: 70,
                bottom: 50
            },
          xAxis: [
              {
              type: 'category',
              axisTick: {
                alignWithLabel: true
              },
              axisLine: {
                onZero: false,
                lineStyle: {
                  color: colors[0]//鼠标提示和X轴的颜色
                }
              },
              axisPointer: {
                label: {
                  formatter: function (params) {
                    return (
                      '运行率  ' +
                      params.value +
                      (params.seriesData.length ? '：' + params.seriesData[0].data : '')
                    );
                  }
                }
              },
              // prettier-ignore
              data: []
            },
            {
              type: 'category',
              axisTick: {
                alignWithLabel: true
              },
              axisLine: {
                onZero: false,
                lineStyle: {
                  color: colors[1]
                }
              },
              axisPointer: {
                label: {
                  formatter: function (params) {
                    return (
                      '报警率 ' +
                      params.value +
                      (params.seriesData.length ? '：' + params.seriesData[0].data : '')
                    );
                  }
                }
              },
              // prettier-ignore
              data: []
            }
  ],
          yAxis: [
    {
      type: 'value'
    }
  ],
          series: [
          {
      name: '运行率',
      type: 'line',
      smooth: true,
      emphasis: {
        focus: 'series'
      },
      data: [

      ]
    },
          {
      name: '报警率',
      type: 'line',
      xAxisIndex: 1,
      smooth: true,
      emphasis: {
        focus: 'series'
      },
      data: [

      ]
    },
  ]
    };
    $.ajax({
        url:"/sky/robot/chart/line/",
        type:"get",
        dataType:"JSON",
        success:function(res){
            // 将后台返回的数据，更新到option中
            if(res.status){
                option.series[0].data = res.data[0];
                option.series[1].data = res.data[1];
                option.xAxis[0].data = res.date;
                option.xAxis[1].data = res.date;
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
    $.get('/sky/robot/status/',function(data,status){

        if(data.status){
            $('#eq_status').text(data.res_list.sys_status);
            $('#eq_work_status').text(data.res_list.work_status);
            $('#eq_order').text(data.res_list.work_order);
            $('#eq_error').text(data.res_list.work_error);
            $('#eq_output_now').text(data.res_list.work_output);
            $('#eq_output_total').text(data.res_list.total_output);
            $('#eq_xspeed').text(data.res_list.x_speed);
            $('#eq_yspeed').text(data.res_list.y_speed);
            $('#eq_zspeed').text(data.res_list.z_speed);
            $('#eq_cspeed').text(data.res_list.c_speed/100);
            $('#eq_rspeed').text(data.res_list.r_speed/100);
        }else{
            console.log('接口错误')
        };

    });

}

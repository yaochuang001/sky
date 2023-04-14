
$(function(){
    EqName = $('#eq_name').html();
    console.log(name);
    initLine();
    initBar();
    initStatus();
    setInterval(initLine,5000);
    setInterval(initBar,5000);
    setInterval(initStatus,5000);
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
        url:"/sky/dg/chart/self_op/",
        type:"post",
        data:{'name':EqName},
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
                      '运行时间  ' +
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
                      '停机时间 ' +
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
      name: '运行时间',
      type: 'line',
      smooth: true,
      emphasis: {
        focus: 'series'
      },
      data: [

      ]
    },
          {
      name: '停机时间',
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
        url:"/sky/dg/chart/self_eff/",
        type:"post",
        data:{'name':EqName},
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
    $.post('/sky/dg/chart/self_sta/',{'name':EqName},function(data,status){

        if(data.status){
            $('#eq_status').text(data.res_list.sys_status);
            $('#eq_total_op').text(data.res_list.total_output);
            $('#eq_order').text();
            $('#eq_efficiency').text(data.res_list.efficiency);
            $('#eq_output_now').text(data.res_list.op_everyday);
            $('#eq_work_time').text(data.res_list.work);
            $('#eq_efficiency_avg').text(data.res_list.efficiency_avg);
            $('#eq_week').text(data.res_list.week_output);
        }else{
            console.log('接口错误')
        };

    });

}

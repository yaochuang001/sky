
$(function(){
    initLine();
    initBar();
    initPie();
    setInterval(initBar,5000);
})

function initBar(){
    // 基于准备好的dom，初始化echarts实例
    console.log('222222');
    var myChart = echarts.init(document.getElementById('m2'));

    // 指定图表的配置项和数据
    var option = {
       title: {
          text: '月度产量-计划',
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

    $.ajax({
        url:"/chart/bar/",
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
                    console.log('resize')
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
    option = {
  title: {
    text: '医用注塑设备',
    subtext: 'Work Status',
    left: 'center'
  },
  tooltip: {
    trigger: 'item'
  },
  legend: {
    bottom:0,
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      radius: '50%',
      data: [
        { value: 1048, name: '生产中' },
        { value: 735, name: '调试中' },
        { value: 284, name: '停机中' },
        { value: 150, name: '计划停机' }
      ],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }
  ]
};

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    window.addEventListener('resize', () => {
        console.log('resize')
        myChart.resize()
        });

}


function initLine(){
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('m1'));

    // 指定图表的配置项和数据
    const colors = ['#5470C6', '#EE6666'];
    option = {
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
              color: colors[1]
            }
          },
          axisPointer: {
            label: {
              formatter: function (params) {
                return (
                  'Precipitation  ' +
                  params.value +
                  (params.seriesData.length ? '：' + params.seriesData[0].data : '')
                );
              }
            }
          },
          // prettier-ignore
          data: ['2023-1', '2023-2', '2023-3', '2023-4', '2023-5', '2023-6', '2023-7', '2023-8', '2023-9', '2023-10', '2023-11', '2023-12']
        },
        {
          type: 'category',
          axisTick: {
            alignWithLabel: true
          },
          axisLine: {
            onZero: false,
            lineStyle: {
              color: colors[0]
            }
          },
          axisPointer: {
            label: {
              formatter: function (params) {
                return (
                  'Precipitation  ' +
                  params.value +
                  (params.seriesData.length ? '：' + params.seriesData[0].data : '')
                );
              }
            }
          },
          // prettier-ignore
          data: ['2022-1', '2022-2', '2022-3', '2022-4', '2022-5', '2022-6', '2022-7', '2022-8', '2022-9', '2022-10', '2022-11', '2022-12']
        }
      ],
      yAxis: [
        {
          type: 'value'
        }
      ],
      series: [
        {
          name: '完成度(2022)',
          type: 'line',
          xAxisIndex: 1,
          smooth: true,
          emphasis: {
            focus: 'series'
          },
          data: [
            106.3, 105.3, 104.7, 94.8, 104.8, 95.4, 105.4, 107.2, 106.7, 110.2, 110.5, 102.3
          ]
        },
        {
          name: '完成度(2023)',
          type: 'line',
          smooth: true,
          emphasis: {
            focus: 'series'
          },
          data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
          ]
        }
      ]
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    window.addEventListener('resize', () => {
        console.log('resize')
        myChart.resize()
        });

}



$(function(){
    initBar();
    initPie();
})

function initBar(){
    // 基于准备好的dom，初始化echarts实例
    console.log('kaishile');
    var myChart = echarts.init(document.getElementById('m2'));

    // 指定图表的配置项和数据
    var option = {
title: {
  text: '员工1业绩',
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
    text: 'Referer of a Website',
    subtext: 'Fake Data',
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
        { value: 1048, name: 'Search Engine' },
        { value: 735, name: 'Direct' },
        { value: 580, name: 'Email' },
        { value: 484, name: 'Union Ads' },
        { value: 300, name: 'Video Ads' }
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
                    console.log('resize');
                    myChart.resize();
                });

}


import datetime
import calendar
# 聚合函数
from django.db import connection, close_old_connections
Week = ['星期一','星期二','星期三','星期四','星期五','星期六','星期天']
# 获取当前时间的周时间
def get_monday_to_sunday(today, weekly=0):
    """
    :function: 获取指定日期的周一周的日期
    :param today: '2021-11-16'; 当前日期：today = datetime.now().strftime('%Y-%m-%d')
    :param weekly: 获取指定日期的上几周或者下几周，weekly=0当前周，weekly=-1上一周，weekly=1下一周
    :return: 返回一个日期键值对
    :return_type: tuple
    """
    last = weekly * 7
    today = datetime.datetime.strptime(str(today), "%Y-%m-%d")
    monday = datetime.datetime.strftime(today - datetime.timedelta(today.weekday() - last), "%Y-%m-%d")
    monday_ = datetime.datetime.strptime(monday, "%Y-%m-%d")
    sunday = datetime.datetime.strftime(monday_ + datetime.timedelta(monday_.weekday() + 6), "%Y-%m-%d")
    tuesday = datetime.datetime.strftime(monday_ + datetime.timedelta(monday_.weekday() + 1), "%Y-%m-%d")
    wednesday = datetime.datetime.strftime(monday_ + datetime.timedelta(monday_.weekday() + 2), "%Y-%m-%d")
    thursday = datetime.datetime.strftime(monday_ + datetime.timedelta(monday_.weekday() + 3), "%Y-%m-%d")
    friday = datetime.datetime.strftime(monday_ + datetime.timedelta(monday_.weekday() + 4), "%Y-%m-%d")
    saturday = datetime.datetime.strftime(monday_ + datetime.timedelta(monday_.weekday() + 5), "%Y-%m-%d")

    #return {'monday':monday,'tuesday':tuesday,'wednesday':wednesday,'thursday':thursday,'friday':friday,
            #'saturday':saturday,'sunday':sunday}
    return [monday,tuesday,wednesday,thursday,friday,saturday,sunday]

# 获取当前时间的月时间
def get_month(year, month):
    """
    输入int year int month，获取list[]
    example:['2022.11.1', '2022.11.2', '2022.11.3', '2022.11.4', '2022.11.5', '2022.11.6',
     '2022.11.7', '2022.11.8', '2022.11.9', '2022.11.10', '2022.11.11', '2022.11.12', '2022.11.13',
     '2022.11.14', '2022.11.15', '2022.11.16', '2022.11.17', '2022.11.18', '2022.11.19', '2022.11.20',
      '2022.11.21', '2022.11.22', '2022.11.23', '2022.11.24', '2022.11.25', '2022.11.26', '2022.11.27',
      '2022.11.28', '2022.11.29', '2022.11.30']
    """
    month_day = []
    monthRange = calendar.monthrange(year, month)
    for i in range(1, (monthRange[1]+1)):
        if int(month)>=10 and int(i)>=10:
            a = str(year)+'-'+str(month)+'-'+str(i)
            month_day.append(a)
        elif int(month)<10 and int(i)>=10:
            a = str(year) + '-' + '0' + str(month) + '-' + str(i)
            month_day.append(a)
        elif int(month)>=10 and int(i)<10:
            a = str(year) + '-' + str(month) + '-' + '0' + str(i)
            month_day.append(a)
        else:
            a = str(year) + '-' + '0' + str(month) + '-' + '0' + str(i)
            month_day.append(a)

    return month_day

# 获取当周的总结数据
def get_week_data(str):
    """
    :param str: str的值代表要获取的参数：3总产、4运行时间、5调试时间、6平均效率
    :return:{"星期一": 188, "星期二": 0, "星期三": 0, "星期四": 0, "星期五": 0, "星期六": 0, "星期天": 0, "结果": "OK"}
    """
    try:
        context = {}
        b = []
        #获取当前时间
        t = datetime.datetime.now().strftime('%Y-%m-%d')
        # 获取当前周时间
        a = get_monday_to_sunday(today=t,weekly=0)
        sql = "select * from sky_robotstatus where YEARWEEK(date_format(c_time,'%Y-%m-%d'),1)=YEARWEEK(now(),7)"
        cursor = connection.cursor()
        cursor.execute(sql)
        ret = cursor.fetchall()
        ret = list(ret)
        if len(ret) !=0:
            for r in ret:
                context[r[8]]=r[str]# r[8]获取数据中存储的日期字符串example'2023-04-08'
                b.append(r[8])
            out = list(set(a).difference(set(b)))
            for o in out:
                context[o]=0
            # {'2023-04-08': 845, '2023-04-09': 2099, '2023-04-06': 0, '2023-04-04': 0, '2023-04-07': 0, '2023-04-03': 0, '2023-04-05': 0}
            # [('2023-04-03', 0), ('2023-04-04', 0), ('2023-04-05', 0), ('2023-04-06', 0), ('2023-04-07', 0), ('2023-04-08', 845), ('2023-04-09', 2099)]
            lst_sort = sorted(context.items(), key=lambda k: k[0])# 按照日期进行排序
            context = {}
            i = 0
            for lst in lst_sort:
                context[Week[i]] = lst[1]
                i +=1
        else:
            for j in range(0,7):
                context[Week[j]] = 0
        context['结果'] = 'OK'
    except Exception as e:
        print(e)
        context = {'结果':str(e)}
    return context


def get_last_week_data(str):
    """
    :param str: str的值代表要获取的参数：3总产、4运行时间、5调试时间、6平均效率
    :return:{"星期一": 188, "星期二": 0, "星期三": 0, "星期四": 0, "星期五": 0, "星期六": 0, "星期天": 0, "结果": "OK"}
    """
    try:
        context = {}
        b = []
        #获取当前时间
        t = datetime.datetime.now().strftime('%Y-%m-%d')
        # 获取当前周时间
        a = get_monday_to_sunday(today=t,weekly=-1)
        sql = "select * from sky_robotstatus where YEARWEEK(date_format(c_time,'%Y-%m-%d'),1)=YEARWEEK(now(),7)-1"
        cursor = connection.cursor()
        cursor.execute(sql)
        ret = cursor.fetchall()
        ret = list(ret)
        if len(ret) !=0:
            for r in ret:
                context[r[8]]=r[str]# r[8]获取数据中存储的日期字符串example'2023-04-08'
                b.append(r[8])
            out = list(set(a).difference(set(b)))
            for o in out:
                context[o]=0
            # {'2023-04-08': 845, '2023-04-09': 2099, '2023-04-06': 0, '2023-04-04': 0, '2023-04-07': 0, '2023-04-03': 0, '2023-04-05': 0}
            # [('2023-04-03', 0), ('2023-04-04', 0), ('2023-04-05', 0), ('2023-04-06', 0), ('2023-04-07', 0), ('2023-04-08', 845), ('2023-04-09', 2099)]
            lst_sort = sorted(context.items(), key=lambda k: k[0])# 按照日期进行排序
            context = {}
            i = 0
            for lst in lst_sort:
                context[Week[i]] = lst[1]
                i +=1
        else:
            for j in range(0,7):
                context[Week[j]] = 0
        context['结果'] = 'OK'
    except Exception as e:
        print(e)
        context = {'结果':str(e)}
    return context


# 获取当月的总结数据
def get_month_data(str):
    """
    :param str: str的值代表要获取的参数：3总产、4运行时间、5调试时间、6平均效率
    :return:{"星期一": 188, "星期二": 0, "星期三": 0, "星期四": 0, "星期五": 0, "星期六": 0, "星期天": 0, "结果": "OK"}
    """
    try:
        context = {}
        b = []
        today = datetime.date.today()
        a = get_month(year=int(today.year),month=int(today.month))
        # print(a)
        sql = "select * from data_everyday where date_format(c_time,'%Y-%m')=date_format(now(),'%Y-%m');"
        cursor = connection.cursor()
        cursor.execute(sql)
        ret = cursor.fetchall()
        ret = list(ret)
        if len(ret) !=0:
            for r in ret:
                context[r[2]]=r[str]
                b.append(r[2])
            out = list(set(a).difference(set(b)))
            for o in out:
                context[o]=0
            # print(context)
        else:
            for j in range(0,(len(a)+1)):
                context[a[j]] = 0
        context['结果'] = 'OK'
    except Exception as e:
        print(e)
        context = {'结果':str(e)}
    context_date = {'日期':a,'数据':context}
    return context_date


# 获取当周的东莞数据
def get_week_dg_data(str,name):
    """
    :param str: str的值代表要获取的参数：3总产、4运行时间、5调试时间、6平均效率
    :return:{"星期一": 188, "星期二": 0, "星期三": 0, "星期四": 0, "星期五": 0, "星期六": 0, "星期天": 0, "结果": "OK"}
    """
    try:
        context = {}
        b = []
        #获取当前时间
        t = datetime.datetime.now().strftime('%Y-%m-%d')
        # 获取当前周时间
        a = get_monday_to_sunday(today=t,weekly=0)
        sql =  "select * from sky_dgstatus where YEARWEEK(date_format(c_time,'%%Y-%%m-%%d'),1)=YEARWEEK(now(),7) " \
                    "and id in(select max(id)from sky_dgstatus where name='%s' group by time);"%(name)
        cursor = connection.cursor()
        cursor.execute(sql)
        ret = cursor.fetchall()
        ret = list(ret)
        if len(ret) !=0:
            for r in ret:
                context[r[7]]=r[str]# r[7]获取数据中存储的日期字符串example'2023-04-08'
                b.append(r[7])
            out = list(set(a).difference(set(b)))
            for o in out:
                context[o]=0
            # {'2023-04-08': 845, '2023-04-09': 2099, '2023-04-06': 0, '2023-04-04': 0, '2023-04-07': 0, '2023-04-03': 0, '2023-04-05': 0}
            # [('2023-04-03', 0), ('2023-04-04', 0), ('2023-04-05', 0), ('2023-04-06', 0), ('2023-04-07', 0), ('2023-04-08', 845), ('2023-04-09', 2099)]
            lst_sort = sorted(context.items(), key=lambda k: k[0])# 按照日期进行排序
            context = {}
            i = 0
            for lst in lst_sort:
                context[Week[i]] = lst[1]
                i +=1
        else:
            for j in range(0,7):
                context[Week[j]] = 0
        context['结果'] = 'OK'
    except Exception as e:
        print(e)
        context = {'结果':str(e)}
    return context

# 获取上周的东莞数据
def get_lastweek_dg_data(str,name):
    """
    :param str: str的值代表要获取的参数：3总产、4运行时间、5调试时间、6平均效率
    :return:{"星期一": 188, "星期二": 0, "星期三": 0, "星期四": 0, "星期五": 0, "星期六": 0, "星期天": 0, "结果": "OK"}
    """
    try:
        context = {}
        b = []
        #获取当前时间
        t = datetime.datetime.now().strftime('%Y-%m-%d')
        # 获取当前周时间
        a = get_monday_to_sunday(today=t,weekly=-1)
        sql =  "select * from sky_dgstatus where YEARWEEK(date_format(c_time,'%%Y-%%m-%%d'),1)=YEARWEEK(now(),7)-1 " \
                    "and id in(select max(id)from sky_dgstatus where name='%s' group by time);"%(name)
        cursor = connection.cursor()
        cursor.execute(sql)
        ret = cursor.fetchall()
        ret = list(ret)
        print(ret  )
        if len(ret) !=0:
            for r in ret:
                context[r[7]]=r[str]# r[7]获取数据中存储的日期字符串example'2023-04-08'
                b.append(r[7])
            out = list(set(a).difference(set(b)))
            for o in out:
                context[o]=0
            # {'2023-04-08': 845, '2023-04-09': 2099, '2023-04-06': 0, '2023-04-04': 0, '2023-04-07': 0, '2023-04-03': 0, '2023-04-05': 0}
            # [('2023-04-03', 0), ('2023-04-04', 0), ('2023-04-05', 0), ('2023-04-06', 0), ('2023-04-07', 0), ('2023-04-08', 845), ('2023-04-09', 2099)]
            lst_sort = sorted(context.items(), key=lambda k: k[0])# 按照日期进行排序
            context = {}
            i = 0
            for lst in lst_sort:
                context[Week[i]] = lst[1]
                i +=1
        else:
            for j in range(0,7):
                context[Week[j]] = 0
        context['结果'] = 'OK'
    except Exception as e:
        print(e)
        context = {'结果':str(e)}
    return context
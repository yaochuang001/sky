# import datetime
# # current_date = datetime.datetime.now().strftime('%Y-%m-%d')
# # print(current_date)
# current_date = datetime.datetime.now().strftime('%Y-%m')
# # current_date = datetime.datetime.now().date()
# print(current_date)
# now_time = datetime.datetime.now()
# print(now_time.month)
import datetime
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet


# 读取excel表格中的日期
def xldate_as_datetime(xldate, datemode=0):
    if datemode not in (0, 1):
        raise Exception(datemode)
    if xldate == 0.00:
        return datetime.time(0, 0, 0)
    if xldate < 0.00:
        raise Exception(xldate)
    xldays = int(xldate)
    frac = xldate - xldays
    seconds = int(round(frac * 86400.0))
    assert 0 <= seconds <= 86400
    if seconds == 86400:
        seconds = 0
        xldays += 1
    # if xldays >= _XLDAYS_TOO_LARGE[datemode]:
    #    raise XLDateTooLarge(xldate)
    if xldays == 0:
        # second = seconds % 60; minutes = seconds // 60
        minutes, second = divmod(seconds, 60)
        # minute = minutes % 60; hour    = minutes // 60
        hour, minute = divmod(minutes, 60)
        return datetime.time(hour, minute, second)
    if xldays < 61 and datemode == 0:
        raise Exception(xldate)
    return (
            datetime.date.fromordinal(xldays + 693594 + 1462 * datemode)
            + datetime.timedelta(seconds=seconds)
    )


# if __name__ == '__main__':
#     # 读取excel
#     workbook = openpyxl.load_workbook("D:\pythonwork\mindscrapy\朱志文.xlsx")
#     # 获取工作簿
#     sheet: Worksheet = workbook['Sheet1']
#     # 获取S列
#     sl = sheet['S']
#     temp = None
#     for s in sl:
#         value = s.value
#         if value is not None:
#             # 私有方法-数字转成日期
#             t = xldate_as_datetime(value)
#             # 去掉时间，保留日期
#             as_datetime = str(t)[0:10]
#             # 重新赋值
#             s.value = as_datetime
#             # 修改临时值
#             temp = as_datetime
#         else:
#             # 如果是空的，采用上一个值
#             s.value = temp
#     # 保存为新的excel
#     workbook.save('D:\pythonwork\mindscrapy\朱志文00.xlsx')

t = xldate_as_datetime(44820)
print(t)
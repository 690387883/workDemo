# math 函數
# import math 
# print(math.floor(22.22)) # 22 向下取整
# print(math.ceil(22.22)) # 23 向上取整


# datetime 函數

import datetime

# print(datetime.datetime(2022, 1, 1))  # 指定时间 2022-01-01 00:00:00
# print(datetime.datetime.now()) # 当前时间
# print(datetime.datetime.today()) # 当前时间
# print(datetime.date(2023,2,2)) # 当前时间 2023-02-02
# print(datetime.time(23,59,58)) # 时分秒 23:59:58

# 计算未来和过去时间，days,seconds秒 hours、weeks minute ...
# nowDate = datetime.datetime.today()

# nowDate +=datetime.timedelta(hours=24)
# print(nowDate)

# 日期跟字符串转换

print(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
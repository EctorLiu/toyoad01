    ##### INDEX ######
# def RS_DateTime_2_YYYYMMDD_HHNNSS():
# def RS_DateTime_2_YYYYMMDD_HHNN():
# def RS_DateTime_2_YYYYMMDD():
# def RS_DateTime_2_HHNNSS():
# def RS_DateTime_2_HHNN():
    # ***** ***** ***** ***** *****

    ##### 時間函數 ######
from datetime import datetime
import time

GVdatNow = datetime.now()
GVstrToday = GVdatNow.strftime("%Y-%m-%d") 
GVstrNow = GVdatNow.strftime("%Y-%m-%d %H:%M:%S") 

# FVstrLCNow = time.strftime("%Y-%m-%d %H:%M:%S.%f", time.localtime())
GVstrGMNow = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
GVdatGMNow = datetime.strptime(GVstrGMNow, "%Y-%m-%d %H:%M:%S") 
    # ***** ***** ***** ***** *****


    ##### 程式區域 ######
    ##### 程式區域 ######
    ##### 程式區域 ######
    ##### 程式區域 ######
    ##### 程式區域 ######
    ##### 程式區域 ######
    ##### 程式區域 ######
    ##### 程式區域 ######
    ##### 程式區域 ######
    ##### 程式區域 ######

def RS_DateTime_2_YYYYMMDD_HHNNSS():
    datDT = time.localtime()
    strYear = time.strftime("%Y", datDT) 
    strMonth = time.strftime("%m", datDT) 
    strDay = time.strftime("%d", datDT) 
    strHour = time.strftime("%H", datDT) 
    strMinute = time.strftime("%M", datDT) 
    strSecond = time.strftime("%S", datDT) 
    if len(strMonth) < 2:
        strMonth = '0' + strMonth
    if len(strDay) < 2:
        strDay = '0' + strDay
    if len(strHour) < 2:
        strHour = '0' + strHour
    if len(strMinute) < 2:
        strMinute = '0' + strMinute
    if len(strSecond) < 2:
        strSecond = '0' + strSecond
    RS_DateTime_2_YYYYMMDD_HHNNSS = strYear + strMonth + strDay + '_' + strHour + strMinute + strSecond
    return RS_DateTime_2_YYYYMMDD_HHNNSS

def RS_DateTime_2_YYYYMMDD_HHNN():
    datDT = time.localtime()
    strYear = time.strftime("%Y", datDT) 
    strMonth = time.strftime("%m", datDT) 
    strDay = time.strftime("%d", datDT) 
    strHour = time.strftime("%H", datDT) 
    strMinute = time.strftime("%M", datDT) 
    if len(strMonth) < 2:
        strMonth = '0' + strMonth
    if len(strDay) < 2:
        strDay = '0' + strDay
    if len(strHour) < 2:
        strHour = '0' + strHour
    if len(strMinute) < 2:
        strMinute = '0' + strMinute
    RS_DateTime_2_YYYYMMDD_HHNN = strYear + strMonth + strDay + '_' + strHour + strMinute
    return RS_DateTime_2_YYYYMMDD_HHNN

def RS_DateTime_2_YYYYMMDD():
    datDT = time.localtime()
    strYear = time.strftime("%Y", datDT) 
    strMonth = time.strftime("%m", datDT) 
    strDay = time.strftime("%d", datDT) 
    if len(strMonth) < 2:
        strMonth = '0' + strMonth
    if len(strDay) < 2:
        strDay = '0' + strDay
    RS_DateTime_2_YYYYMMDD = strYear + strMonth + strDay
    return RS_DateTime_2_YYYYMMDD

def RS_DateTime_2_HHNNSS():
    datDT = time.localtime()
    strHour = time.strftime("%H", datDT) 
    strMinute = time.strftime("%M", datDT) 
    strSecond = time.strftime("%S", datDT) 
    if len(strHour) < 2:
        strHour = '0' + strHour
    if len(strMinute) < 2:
        strMinute = '0' + strMinute
    if len(strSecond) < 2:
        strSecond = '0' + strSecond
    RS_DateTime_2_HHNNSS = strHour + strMinute + strSecond
    return RS_DateTime_2_HHNNSS

def RS_DateTime_2_HHNN():
    datDT = time.localtime()
    strHour = time.strftime("%H", datDT) 
    strMinute = time.strftime("%M", datDT) 
    if len(strHour) < 2:
        strHour = '0' + strHour
    if len(strMinute) < 2:
        strMinute = '0' + strMinute
    RS_DateTime_2_HHNN = strHour + strMinute
    return RS_DateTime_2_HHNN
    # ***** ***** ***** ***** *****

    ##### 備註區域 ######
# 时间日期符号：  
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身
    # ***** ***** ***** ***** *****

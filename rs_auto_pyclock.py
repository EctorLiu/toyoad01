    ##### 匯入函式庫 ######
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()

import urllib.request
    # ***** ***** ***** ***** *****


    ##### 自動執行程式 ######
@sched.scheduled_job('cron', day_of_week='mon-fri', minute='*/25')

def scheduled_job():
    url = 'https://ector01.herokuapp.com/'
    conn = urllib.request.urlopen(url)
    for key, value in conn.getheaders():
        print(key, value)

sched.start()
    # ***** ***** ***** ***** *****


    ##### 備註區域 ######
# 表示2017年3月22日17时19分07秒执行该程序
# sched.add_job(my_job, 'cron', year=2017,month = 03,day = 22,hour = 17,minute = 19,second = 07)
 
# 表示任务在6,7,8,11,12月份的第三个星期五的00:00,01:00,02:00,03:00 执行该程序
# sched.add_job(my_job, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
 
# 表示从星期一到星期五5:30（AM）直到2014-05-30 00:00:00
# ched.add_job(my_job(), 'cron', day_of_week='mon-fri', hour=5, minute=30,end_date='2014-05-30')
 
# 表示每5秒执行该程序一次，相当于interval 间隔调度中seconds = 5
# sched.add_job(my_job, 'cron',second = '*/5')

# @sched.scheduled_job('cron', day_of_week = 'mon-fri', hour = 11, minute = 35, second = 05)
# @sched.scheduled_job('cron', year = 2021, month = 12, day = 27, hour = 12, minute = 2, second = 30)

# @sched.scheduled_job('cron', year = 2021, month = 12, day = 25, minute = 20)
    # ***** ***** ***** ***** *****

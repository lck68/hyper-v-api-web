import os
import random
from datetime import datetime, timedelta
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
 
if is_admin():
    # 主程序写在这里


    # 设置起始日期和终止日期
    start_date = datetime(2023, 5, 14)  # 修改为你想要的起始日期
    end_date = datetime(2024, 8, 6)   # 修改为你想要的终止日期

    # 定义modify函数
    def modify():
        with open("index.txt", "a") as f:
            f.write('1311')
            f.close

    # 定义生成随机时间的函数
    def suiji_time():
        random_hour = random.randint(8, 21)  # 8点到21点
        random_minute = random.randint(30, 59)  # 11分到59分
        return random_hour, random_minute

    # 循环从起始日期到终止日期执行操作
    current_date = start_date
    while current_date <= end_date:
        os.system(f"date {current_date.strftime('%Y-%m-%d')}")  # 修改系统日期
        # 设置系统时间为当前日期和随机时间
        random_hour, random_minute = suiji_time()
            
        os.system(f"time {random_hour}:{random_minute}")  # 修改系统时间
            # 执行modify函数
        modify()
        input()
        # 增加一天
        current_date += timedelta(days=1)
        print("="*20)
    print("完毕")
    input()

else:
    # 以管理员权限重新运行程序
    ctypes.windll.shell32.ShellExecuteW(None,"runas", sys.executable, __file__, None, 1)

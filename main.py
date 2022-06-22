# from memory_profiler import memory_usage
import time
import requests
import json
import datetime
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY, YEARLY
import matplotlib.pyplot as plt

url = " "
r = requests.get(url)
data = r.json()


# def save():
#     start = time.time()
#     with open('./1.csv', mode = 'w') as f:
#         for i in range(1,len(data)+1,1):
#             df = pd.DataFrame(data[str(i)])
#             df['VALUE'] = pd.to_numeric(df['VALUE'])
#             df.sort_values(['DATETIME'], inplace=True)
#             df.to_csv(f, index=False)
#     end = time.time()
# #     print(memory_usage())
#     print(end - start)

def savedata():
    start = time.time()
    a = (data[str(i)] for i in range(1, 19, 1))
    with open('./2.csv', mode='w') as f:
        for x in a:
            df = pd.DataFrame(x)
            df.sort_values(['DATETIME'], inplace=True)
            df['VALUE'] = pd.to_numeric(df['VALUE'])
            df.to_csv(f, index=False)
    end = time.time()
    print(end - start)
    #     print(memory_usage())
    print("111.csv is ok")

for i in range(1, len(data) + 1, 1):
    df = pd.DataFrame(data[str(i)])
    df.sort_values(['DATETIME'], inplace=True)
    df['VALUE'] = pd.to_numeric(df['VALUE'])
    y = df['VALUE']
    x = df['DATETIME']
    x = pd.to_datetime(x)
    plt.figure(figsize=(20, 20))
    ax = plt.gca()
    plt.grid()
    hoursLoc = mpl.dates.HourLocator(interval=1)
    ax.xaxis.set_minor_locator(hoursLoc)
    ax.xaxis.set_minor_formatter(mdates.DateFormatter("%H"))
    MinuteLocator = mpl.dates.MinuteLocator(interval=1)
    ax.xaxis.set_major_locator(MinuteLocator)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%M"))
    ax.tick_params(pad=10)
    plt.plot(x, y, "o", color="red")
    plt.plot(x, y)
    plt.show()

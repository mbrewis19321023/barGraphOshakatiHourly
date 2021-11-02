# In the below code some varibales are called "Load" or "powerFactor" even
# though that is not the real world phenomenon they represent. This is due to the original datafram column renaming
# if you want to be accurate about variable names as you should. You can change them either here or in the companion script
# called csvToPickle.py


import os
import sys
from matplotlib import colors
from numpy import mod
from openpyxl.styles import NamedStyle, Font, Border, Side
import tkinter as tk
from tkinter import Label, filedialog, Text
import tkinter.font as font
from openpyxl.utils.dataframe import dataframe_to_rows
from tkinter.filedialog import asksaveasfile
from openpyxl.styles import Alignment
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from openpyxl.styles import NamedStyle, Font, Border, Side, numbers
import pandas as pd
import pandas as pd
import datetime
from openpyxl import Workbook
from openpyxl.styles import Font
import re
import matplotlib.pyplot as plt
from collections import deque

f = open("myfile.csv", "w")
gingers = True
digitReplace = re.compile(r"(\d+)(,)(\d+)")
dateModify = re.compile(r"(\d{2})\-(\d{2})\-\d{2}(\d{2})")
regGroup = re.compile(
    r"\"\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",")
monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
             'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

date = []
datetick = 0
load = []
load2019 = []
load2020 = []
load2021 = []
nightLoad = []
time = []
powerFactor = []
timeToInt = 0
xAxisTics19 = []
xAxisTics20 = []
xAxisTics21 = []
xTicks = []


for i in range(24):
    xAxisTics19.append(i-0.2)
    xAxisTics20.append(i)
    xAxisTics21.append(i+0.2)
    xTicks.append(str(i) + ":00")

# df = pd.read_pickle("data.pkl")
# df2 = pd.read_pickle("data2.pkl")
df = pd.read_pickle("dataHourly.pkl")

################################################# this is for max demand per month #################################################
dM = df.groupby(['Year', 'Month']).Load.max().reset_index().copy()
dMS = df.groupby(['Year', 'Month']).Solar.sum().reset_index().copy()
################################################# this is for max demand per month #################################################

################################################# this is for max demand from 1700 - 2400 #################################################
dMStartTime = df.groupby(['Year', 'startTime']).Load.mean().reset_index().copy()
################################################# this is for max demand from 1700 - 2400 #################################################


for x, row in dMStartTime.iterrows():
    ################################################# this is for max demand per month #################################################
    # date.append(str(dM.iloc[x]['Year']) + '-' + str(dM.iloc[x]['Month']))
    # load.append(float(dM.iloc[x]['Load']))
    ################################################# this is for max demand per month #################################################
    print(dMStartTime.iloc[x]['startTime'])
    tempV = str(dMStartTime.iloc[x]['startTime']).replace(":", "")
    if dMStartTime.iloc[x]['Year'] == 19:
        load2019.append(dMStartTime.iloc[x]['Load'])
        time.append(dMStartTime.iloc[x]['startTime'])
    if dMStartTime.iloc[x]['Year'] == 20:
        load2020.append(dMStartTime.iloc[x]['Load'])
    if dMStartTime.iloc[x]['Year'] == 21:
        load2021.append(dMStartTime.iloc[x]['Load'])
    # print(tempV)
    # print(dMStartTime.iloc[x]['startTime'])
    # print()
    datetick = x
for x, row in dM.iterrows():
    date.append(str(dM.iloc[x]['Year']) + '-' + str(dM.iloc[x]['Month']))
    load.append(float(dM.iloc[x]['Load']))

for x, i in enumerate(date):
    a = i.split("-")
    if a[1] == '1.0':
        date[x] = "Jan" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '2.0':
        date[x] = "Feb" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '3.0':
        date[x] = "Mar" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '4.0':
        date[x] = "Apr" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '5.0':
        date[x] = "May" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '6.0':
        date[x] = "Jun" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '7.0':
        date[x] = "Jul" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '8.0':
        date[x] = "Aug" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '9.0':
        date[x] = "Sep" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '10.0':
        date[x] = "Oct" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '11.0':
        date[x] = "Nov" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '12.0':
        date[x] = "Dec" + '-' + "20" + str(a[0].split('.')[0])

# ax = plt.subplot(111)
# ax.bar(date, load, width=0.2, color='b', align='center')
# ax.bar(date, solar, width=0.2, color='r', align='center')
# plt.xticks(rotation = 'vertical')
# plt.show()

# plt.title("Maximum demand per months")
# plt.xticks(rotation='vertical')
# plt.xlabel("Date")
# plt.ylabel("Demand (kVA)")
# plt.plot(date, load, 'bo-', label="Demand", )
# for i, v in enumerate(load):
#     plt.text(i, v + 3, "%d" % v, rotation = 90,ha="center", color = "blue")
# for i, v in enumerate(load):
#     plt.text(i, v + 3, "%d" % v, rotation = 90,ha="center", color = "blue")
# plt.ylim(-10, 100)
# plt.legend()


################################################# should obviously be in a function #################################################
load2019 = deque(load2019)
load2019.rotate(10)
el0 = load2019[10]
el10 = load2019[11]
el11 = load2019[12]
el12 = load2019[13]
el13 = load2019[14]
el14 = load2019[15]
el15 = load2019[16]
el16 = load2019[17]
el17 = load2019[18]
el18 = load2019[19]
el19 = load2019[20]
el1 = load2019[21]
el20 = load2019[22]
el21 = load2019[23]
el22 = load2019[0]
el23 = load2019[1]
load2019[0] = el0
load2019[1] = el1
load2019[10] = el10
load2019[11] = el11
load2019[12] = el12
load2019[13] = el13
load2019[14] = el14
load2019[15] = el15
load2019[16] = el16
load2019[17] = el17
load2019[18] = el18
load2019[19] = el19
load2019[20] = el20
load2019[21] = el21
load2019[22] = el22
load2019[23] = el23
################################################# should obviously be in a function #################################################
load2020 = deque(load2020)
load2020.rotate(10)
el0 = load2020[10]
el10 = load2020[11]
el11 = load2020[12]
el12 = load2020[13]
el13 = load2020[14]
el14 = load2020[15]
el15 = load2020[16]
el16 = load2020[17]
el17 = load2020[18]
el18 = load2020[19]
el19 = load2020[20]
el1 = load2020[21]
el20 = load2020[22]
el21 = load2020[23]
el22 = load2020[0]
el23 = load2020[1]
load2020[0] = el0
load2020[1] = el1
load2020[10] = el10
load2020[11] = el11
load2020[12] = el12
load2020[13] = el13
load2020[14] = el14
load2020[15] = el15
load2020[16] = el16
load2020[17] = el17
load2020[18] = el18
load2020[19] = el19
load2020[20] = el20
load2020[21] = el21
load2020[22] = el22
load2020[23] = el23
################################################# should obviously be in a function #################################################
load2021 = deque(load2021)
load2021.rotate(10)
el0 = load2021[10]
el10 = load2021[11]
el11 = load2021[12]
el12 = load2021[13]
el13 = load2021[14]
el14 = load2021[15]
el15 = load2021[16]
el16 = load2021[17]
el17 = load2021[18]
el18 = load2021[19]
el19 = load2021[20]
el1 = load2021[21]
el20 = load2021[22]
el21 = load2021[23]
el22 = load2021[0]
el23 = load2021[1]
load2021[0] = el0
load2021[1] = el1
load2021[10] = el10
load2021[11] = el11
load2021[12] = el12
load2021[13] = el13
load2021[14] = el14
load2021[15] = el15
load2021[16] = el16
load2021[17] = el17
load2021[18] = el18
load2021[19] = el19
load2021[20] = el20
load2021[21] = el21
load2021[22] = el22
load2021[23] = el23




plt.title("Average Hourly Maximum Demand from Oct 2019 - Oct 2021")
plt.xticks(xAxisTics19 , xTicks ,rotation='vertical')
plt.xlabel("Time", labelpad=20)
plt.ylabel("Average Demand (kVA)")
# plt.plot(xAxisTics, load2019, 'bo-', label="Demand", )
plt.bar(xAxisTics19, load2019, color='#e67e22', width=0.1, label="2019 (Averaged 3 month data set)")
plt.bar(xAxisTics20, load2020, color='green', width=0.1, label="2020 (Averaged 12 month data set)")
plt.bar(xAxisTics21, load2021, color='blue', width=0.1, label="2021 (Averaged 10 month data set)")
for i, v in enumerate(load2019):
    plt.text(i-0.3, v + 1, "%.2f" % v, rotation=90, ha="center", color="#e67e22")
for i, v in enumerate(load2020):
    plt.text(i, v + 1, "%.2f" % v, rotation = 90,ha="center", color = "green")
for i, v in enumerate(load2021):
    plt.text(i+0.3, v + 1, "%.2f" % v, rotation = 90,ha="center", color = "blue")
plt.ylim(0, 66)
plt.legend()


plt.show()

print()
# for j, x in enumerate(lines):
#         p1 = x.replace(';', '","')
#         p1 = x.replace('\n', '')
#         r1 = re.findall(dateModify, p1)
#         p1 = p1.split(",")
#         try:
#             infoPoints.loc[j] = [int(r1[0][2])] + [int(r1[0][1])] + [int(r1[0][0])]  + [p1[1]] + [float(p1[2])] + [float(p1[3])]
#         except IndexError:
#             pass

# infoPoints.to_pickle("data.pkl")
# infoPointsSumDayLoads = infoPoints.groupby(["Day"]).Load.sum().reset_index()
# infoPointsSumDaySolar= infoPoints.groupby(["Day"]).Solar.sum().reset_index()
# ax = infoPointsSumDayLoads.plot(x="Day",y=["Load"])
# infoPointsSumMonthLoads = infoPoints.groupby(["Month"]).Load.sum().reset_index()
# infoPointsSumDaySolar.plot(x="Day",y=["Solar"],ax = ax)
# plt.show()

# try:
#     if r1[0][1]:
#         if r1[0][1] == '01':
#             p5 = re.sub(dateModify, r"\1-Jan-\3", p1)
#         if r1[0][1] == '02':
#             p5 = re.sub(dateModify, r"\1-Feb-\3", p1)
#         if r1[0][1] == '03':
#             p5 = re.sub(dateModify, r"\1-Mar-\3", p1)
#         if r1[0][1] == '04':
#             p5 = re.sub(dateModify, r"\1-Apr-\3", p1)
#         if r1[0][1] == '05':
#             p5 = re.sub(dateModify, r"\1-May-\3", p1)
#         if r1[0][1] == '06':
#             p5 = re.sub(dateModify, r"\1-Jun-\3", p1)
#         if r1[0][1] == '07':
#             p5 = re.sub(dateModify, r"\1-Jul-\3", p1)
#         if r1[0][1] == '08':
#             p5 = re.sub(dateModify, r"\1-Aug-\3", p1)
#         if r1[0][1] == '09':
#             p5 = re.sub(dateModify, r"\1-Sep-\3", p1)
#         if r1[0][1] == '10':
#             p5 = re.sub(dateModify, r"\1-Oct-\3", p1)
#         if r1[0][1] == '11':
#             p5 = re.sub(dateModify, r"\1-Nov-\3", p1)
#         if r1[0][1] == '12':
#             p5 = re.sub(dateModify, r"\1-Dec-\3", p1)
#         p6 = p5.replace(" ", '","')
#         supString = '"","'
#         p7 = supString + p6
#         r2 = re.findall(regGroup, p7)
#         temp5 = float(r2[0][2]) * 2
#         p9 = p7[:22] + ',"blank",' + p7[23:]
# except IndexError:
#   print("oops")

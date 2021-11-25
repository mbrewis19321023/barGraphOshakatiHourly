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


digitReplace = re.compile(r"(\d+)(,)(\d+)")
dateModify = re.compile(r"(\d{2})\-(\d{2})\-\d{2}(\d{2})")
regGroup = re.compile(
    r"\"\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",")
monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
             'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

date = []
datetick = 0
load = []
cons = []
load2019 = []
load2020 = []
load2021 = []
import2019 = []
import2020 = []
import2021 = []
nightLoad = []
time = []
powerFactor = []
timeToInt = 0
xAxisTics19 = []
xAxisTics20 = []
xAxisTics21 = []
xTicks = []

################################################# Toggles what graph to make #################################################
barHourly = 1
consMonthly = 0
################################################# Toggles what graph to make #################################################



for i in range(24):
    xAxisTics19.append(i-0.2)
    xAxisTics20.append(i)
    xAxisTics21.append(i+0.2)
    xTicks.append(str(i) + ":00")

df = pd.read_pickle("dataHourly.pkl")
################################################# this is for max demand per month #################################################
dM = df.groupby(['Year', 'Month']).MaxDemand.max().reset_index().copy()
dMS = df.groupby(['Year', 'Month']).SolarExport.sum().reset_index().copy()
################################################# this is for max demand per month #################################################

################################################# this is for consumption #################################################
dConsum = df.groupby(['Year', 'Month']).ImportActive.sum().reset_index().copy()
################################################# this is for consumption #################################################



################################################# this is for max demand from 1700 - 2400 #################################################
solarExportMeanDFG = df.groupby(['Year', 'startTime']
                         ).SolarExport.mean().reset_index().copy() # to get back make this Load.mean
importActiveMeanDFG = df.groupby(['Year', 'startTime']
                         ).ImportActive.mean().reset_index().copy() 
################################################# this is for max demand from 1700 - 2400 #################################################


for x, row in solarExportMeanDFG.iterrows():
    ################################################# this is for max demand per month #################################################
    # date.append(str(dM.iloc[x]['Year']) + '-' + str(dM.iloc[x]['Month']))
    # load.append(float(dM.iloc[x]['Load']))
    ################################################# this is for max demand per month #################################################
    
    ############# Note that due to the way you set this up initially the variable name remains load2019 
    print(solarExportMeanDFG.iloc[x]['startTime'])
    tempV = str(solarExportMeanDFG.iloc[x]['startTime']).replace(":", "")
    if solarExportMeanDFG.iloc[x]['Year'] == 19:
        load2019.append(solarExportMeanDFG.iloc[x]['SolarExport']) # to get back make this 'Load'
        time.append(solarExportMeanDFG.iloc[x]['startTime'])
    if solarExportMeanDFG.iloc[x]['Year'] == 20:
        load2020.append(solarExportMeanDFG.iloc[x]['SolarExport']) # to get back make this 'Load'
    if solarExportMeanDFG.iloc[x]['Year'] == 21:
        load2021.append(solarExportMeanDFG.iloc[x]['SolarExport']) # to get back make this 'Load'
    # print(tempV)
    # print(dMStartTime.iloc[x]['startTime'])
    # print()
    datetick = x

for x, row in importActiveMeanDFG.iterrows():
    ################################################# this is for max demand per month #################################################
    # date.append(str(dM.iloc[x]['Year']) + '-' + str(dM.iloc[x]['Month']))
    # load.append(float(dM.iloc[x]['Load']))
    ################################################# this is for max demand per month #################################################
    
    ############# Note that due to the way you set this up initially the variable name remains load2019 
    tempV = str(importActiveMeanDFG.iloc[x]['startTime']).replace(":", "")
    if importActiveMeanDFG.iloc[x]['Year'] == 19:
        import2019.append(importActiveMeanDFG.iloc[x]['ImportActive']) # to get back make this 'Load'
        time.append(importActiveMeanDFG.iloc[x]['startTime'])
    if importActiveMeanDFG.iloc[x]['Year'] == 20:
        import2020.append(importActiveMeanDFG.iloc[x]['ImportActive']) # to get back make this 'Load'
    if importActiveMeanDFG.iloc[x]['Year'] == 21:
        import2021.append(importActiveMeanDFG.iloc[x]['ImportActive']) # to get back make this 'Load'
    # print(tempV)
    # print(dMStartTime.iloc[x]['startTime'])
    # print()
    datetick = x

for x, row in dConsum.iterrows():
    date.append(str(dConsum.iloc[x]['Year']) + '-' + str(dConsum.iloc[x]['Month']))
    cons.append(float(dConsum.iloc[x]['ImportActive']))

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




################################################# should obviously be in a function #################################################
try:
    import2019 = deque(import2019)
    import2019.rotate(10)
    el0 = import2019[10]
    el10 = import2019[11]
    el11 = import2019[12]
    el12 = import2019[13]
    el13 = import2019[14]
    el14 = import2019[15]
    el15 = import2019[16]
    el16 = import2019[17]
    el17 = import2019[18]
    el18 = import2019[19]
    el19 = import2019[20]
    el1 = import2019[21]
    el20 = import2019[22]
    el21 = import2019[23]
    el22 = import2019[0]
    el23 = import2019[1]
    import2019[0] = el0
    import2019[1] = el1
    import2019[10] = el10
    import2019[11] = el11
    import2019[12] = el12
    import2019[13] = el13
    import2019[14] = el14
    import2019[15] = el15
    import2019[16] = el16
    import2019[17] = el17
    import2019[18] = el18
    import2019[19] = el19
    import2019[20] = el20
    import2019[21] = el21
    import2019[22] = el22
    import2019[23] = el23
    ################################################# should obviously be in a function #################################################
    import2020 = deque(import2020)
    import2020.rotate(10)
    el0 = import2020[10]
    el10 = import2020[11]
    el11 = import2020[12]
    el12 = import2020[13]
    el13 = import2020[14]
    el14 = import2020[15]
    el15 = import2020[16]
    el16 = import2020[17]
    el17 = import2020[18]
    el18 = import2020[19]
    el19 = import2020[20]
    el1 = import2020[21]
    el20 = import2020[22]
    el21 = import2020[23]
    el22 = import2020[0]
    el23 = import2020[1]
    import2020[0] = el0
    import2020[1] = el1
    import2020[10] = el10
    import2020[11] = el11
    import2020[12] = el12
    import2020[13] = el13
    import2020[14] = el14
    import2020[15] = el15
    import2020[16] = el16
    import2020[17] = el17
    import2020[18] = el18
    import2020[19] = el19
    import2020[20] = el20
    import2020[21] = el21
    import2020[22] = el22
    import2020[23] = el23
    ################################################# should obviously be in a function #################################################
    import2021 = deque(import2021)
    import2021.rotate(10)
    el0 = import2021[10]
    el10 = import2021[11]
    el11 = import2021[12]
    el12 = import2021[13]
    el13 = import2021[14]
    el14 = import2021[15]
    el15 = import2021[16]
    el16 = import2021[17]
    el17 = import2021[18]
    el18 = import2021[19]
    el19 = import2021[20]
    el1 = import2021[21]
    el20 = import2021[22]
    el21 = import2021[23]
    el22 = import2021[0]
    el23 = import2021[1]
    import2021[0] = el0
    import2021[1] = el1
    import2021[10] = el10
    import2021[11] = el11
    import2021[12] = el12
    import2021[13] = el13
    import2021[14] = el14
    import2021[15] = el15
    import2021[16] = el16
    import2021[17] = el17
    import2021[18] = el18
    import2021[19] = el19
    import2021[20] = el20
    import2021[21] = el21
    import2021[22] = el22
    import2021[23] = el23
except IndexError:
    pass


################################################# should obviously be in a function #################################################
try:
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
except IndexError:
    pass



if (barHourly == 1):
    plt.title("Average Solar Export vs Average Import from CENORED per hour averaged over the year 2020")
    plt.xticks(xAxisTics20, xTicks, rotation='vertical')
    plt.xlabel("Time", labelpad=20)
    # plt.plot(xAxisTics20, load2019, 'bo-', label="Demand", )
    # plt.bar(xAxisTics19, load2019, color='#e67e22', width=0.1,
    #         label="2019 (Averaged 3 month data set)")
    plt.bar(xAxisTics20, load2020, color='green', width=0.1,
            label="Export To Cenored (VAh)")
    plt.bar(xAxisTics21, import2020, color='blue', width=0.1,
              label="Import From Cenored (Wh)")
    # for i, v in enumerate(load2019):
    #     plt.text(i-0.3, v + 1, "%.2f" %
    #              v, rotation=90, ha="center", color="#e67e22")
    for i, v in enumerate(load2020):
        plt.text(i, v + 100, "%.2f" % v, rotation=90, ha="center", color="green")
    for i, v in enumerate(import2020):
        plt.text(i+0.3, v + 100, "%.2f" % v, rotation=90, ha="center", color="blue")
    plt.ylim(0, 5000)
    plt.legend()

elif (consMonthly == 1):
     plt.title("Consumption")
     plt.plot(date, cons, 'bo-', label="Consumption", )
     for i, v in enumerate(cons):
        plt.text(i, v + 10000, "%.2f" % v, rotation=90, ha="center", color="blue")
plt.show()

print()

import os
import sys
from numpy import mod
from openpyxl.styles import NamedStyle, Font, Border, Side
import tkinter as tk
from tkinter import filedialog, Text
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

flag = 0
temp = 0

csvFile = open("we.csv")
lines = csvFile.readlines()
# testList = ['6.0', ' 5.291502622129181', ' 8.0', ' 8.0', ' 2019-10-01', ' 02:00:00']


column_names = ["Year", "Month", "Day", "startTime", "Load", "Solar"]
df = pd.DataFrame(columns=column_names)
# df.loc[6] = testList
# df = df.append(testList)

for x, i in enumerate(lines):
    p1 = i.split(",")
    try:

        if flag == 2:
            tempList = [int(p2[0]),p2[1],p2[2],p3,temp/2,0]
            df.loc[x] = tempList
            flag = 0
            temp = 0

        p2 = p1[4].split("-")
        p2[0] = p2[0].replace(" ","")
        p2[0] = int(p2[0][2:])
        p2[1] = int(p2[1])
        p2[2] = int(p2[2])


        p3 = p1[5].split(":")  
        p3[0] = int(p3[0])
        p3 = str(p3[0]) + ":" + p3[1] 
        p3 = p3.replace(" ","")

        temp = float(temp) + float(p1[3]) 
        flag += 1
        
    except:
        pass
df.to_pickle("./dataHourly.pkl")

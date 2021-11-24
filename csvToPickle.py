############################################### LIBRARY #############################################################
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
dateModify = re.compile(r"(\d{2})\-(\d{2})\-\d{2}(\d{2})")
############################################### LIBRARY #############################################################
#
#
############################################### THIS IS A FLAG SYSTEM TO READ TWO LINES INSTEAD OF 1 (FOR HOURLY I.O. HALF HOURLY) #############################################################
flag = 0
tempSolar = 0
tempLoad = 0
############################################### THIS IS A FLAG SYSTEM TO READ TWO LINES INSTEAD OF 1 (FOR HOURLY I.O. HALF HOURLY) #############################################################
#
#
############################################### READ IN THE FILE #############################################################
csvFile = open("cenored.csv")
# csvFile = open("pnpscada.csv")
lines = csvFile.readlines()
############################################### READ IN THE FILE #############################################################
#
#
############################################### MAKE THE DATA FRAME #############################################################
column_names = ["Year", "Month", "Day", "startTime", "Load", "Solar"]
# df = pd.DataFrame(columns=column_names) This is the original code and should be restored
dfS = pd.DataFrame(columns=column_names)
dfC = pd.DataFrame(columns=column_names)
############################################### MAKE THE DATA FRAME #############################################################
#
#
############################################### MAKE THE DATA FRAME A PICKEL FROM PNPSCADA #############################################################
if (csvFile.name == "pnpscada.csv"):
    for x, i in enumerate(lines):
        p1 = i.split(",")
        try:

            if flag == 2:
                tempList = [int(p2[0]), p2[1], p2[2], p3, temp/2, 0]
                dfS.loc[x] = tempList
                flag = 0
                temp = 0

            p2 = p1[4].split("-")
            p2[0] = p2[0].replace(" ", "")
            p2[0] = int(p2[0][2:])
            p2[1] = int(p2[1])
            p2[2] = int(p2[2])

            p3 = p1[5].split(":")
            p3[0] = int(p3[0])
            p3 = str(p3[0]) + ":" + p3[1]
            p3 = p3.replace(" ", "")

            temp = float(temp) + float(p1[3])
            flag += 1

        except:
            pass
    dfS.to_pickle("./dataHourly.pkl")
############################################### MAKE THE DATA FRAME A PICKEL FROM PNPSCADA #############################################################
#
#
############################################### MAKE THE DATA FRAME A PICKEL FROM CENORED #############################################################
elif (csvFile.name == "cenored.csv"):
    for x, i in enumerate(lines):
        p1 = i.split(";")
        pTest = p1[0].replace("/", "-")
        if re.findall(dateModify, pTest):
            try:
                p3 = p1[0].replace("/", "-")
                r2 = re.findall(dateModify, p3)
                o1 = p3.split(" ")
                p1[6] = p1[6].replace(" ", "")
                p1[4] = p1[4].replace(" ", "")
                flag += 1
                tempLoad = float(tempLoad) + float(p1[6])
                tempSolar = float(tempSolar) + float(p1[4])

                if (flag == 2):

                    tempList = [int(r2[0][2]), int(r2[0][1]), int(
                        r2[0][0]), o1[1], tempLoad/2, tempSolar/2]
                    dfC.loc[x] = tempList
                    tempLoad = 0
                    tempSolar = 0
                    flag = 0

            except:
                pass
dfC.to_pickle("./dataHourly.pkl")
############################################### MAKE THE DATA FRAME A PICKEL FROM CENORED #############################################################

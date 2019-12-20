# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# UIN:          528000393
# Name: 		Alex Tung
# Section:		552
# Assignment:	Lab 10B (e.g. Lab 1b-2)
# Date:		2 11 2019

import numpy as np
import matplotlib.pyplot as plt
# Getting points for coordinates
with open("WeatherDataWindows.csv", "r") as info:
    linereader = info.readlines()
    x = []
    y1 = []
    y2 = []
    dew = []
    rain = []
    high = []
    low = []
    for i in linereader:
        values = i.split(',')
        if values[2] != "Temp Avg":
            y1.append(float(values[2]))
        if values[0] != "Date":
            x.append(values[0])
        if values[11] != "Pressure Avg":
            y2.append(float(values[11]))
        if values[5] != "Dew Point Avg":
            dew.append(float(values[5]))
        if values[13] != "Precipitation (in.)\n":
            rain.append(float(values[13]))
        if values[1] != "Temp High":
            high.append(float(values[1]))
        if values[3] != "Temp Low":
            low.append(float(values[3]))
# Line graph
    chart, a1 = plt.subplots()

    color = 'tab:red'
    a1.set_xlabel('Date')
    a1.set_ylabel('Average Temperature', color=color)
    a1.plot(x, y1, color=color)

    a2 = a1.twinx()

    color = 'tab:green'
    a2.set_ylabel('Average Pressure', color=color)
    a2.plot(x, y2, color=color)

    chart.tight_layout()
    plt.xticks(np.arange(0, 1100, 200))
    plt.title("Temperature Average and Pressure Average")
    plt.show()
# Scatter plot
    color = "tab:blue"
    plt.scatter(dew, y1, c=color)
    plt.xlabel("Dew Point Average")
    plt.ylabel("Temperature Average")
    plt.title("Temperature Average and Dew Point Average")
    plt.show()
# Histogram
    n, bins, patches = plt.hist(rain, 50, density=1, facecolor='g')
    plt.xlabel("Precipitation (in.)")
    plt.ylabel("Days")
    plt.title("Precipitation (in.) Over Time")
    plt.show()

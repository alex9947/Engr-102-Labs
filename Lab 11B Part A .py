# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# UIN:          528000393
# Name: 		Alex Tung
# Section:		552
# Assignment:	Lab 11B (e.g. Lab 1b-2)
# Date:		06 11 2019

import numpy as np

file = input("Enter name of file with extension: ")
dimen = 2
x = float(input("Enter X value: "))
information = np.loadtxt(file)


def inter(list1, list2, dim, x):
    lists = []
    for i in range(1, dim):
        formula = list1[i] + (x - list1[0]) * ((list2[i] - list2[0])/(list1[i] - list1[0]))
        lists.append(formula)
    return lists


def sort_info(info, x):
    newinfo = info[info[:, 0].argsort()]
    for i in range(len(info)-1):
        if newinfo[i][0] < x and newinfo[i+1][0] > x:
            return newinfo[i], newinfo[i+1]
    return newinfo[0], newinfo[-1]


mins, maxs = sort_info(information, x)
y = inter(mins, maxs, dimen, x)

print("Interpolated data at x =", x, "is", y, end="")

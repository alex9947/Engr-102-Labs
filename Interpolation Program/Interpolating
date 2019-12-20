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


def inter(list1, list2, dim, x):
    """Calculation of interpolation"""
    answerlist = []
    answerlist.append(x)
    for i in range(1, dim):
        interp = list1[i] + (x - list1[0]) * ((list2[i] - list2[0])/(list1[i] - list1[0]))
        answerlist.append(interp)
    return answerlist


def data_cleanup(data, x):
    """Sorting data"""
    new_data = data[data[:, 0].argsort()]
    for i in range(len(data)-1):
        if new_data[i][0] < x and new_data[i+1][0] > x:
            return new_data[i], new_data[i+1]
    return new_data[0], new_data[-1]


def data_gathering(file_name):
    """User inputted query value & function calls"""
    dimensions = int(input("Enter # of dimensions: "))
    query = float(input("Enter X value: "))
    data = np.loadtxt(file_name)
    min_list, max_list = data_cleanup(data, query)
    answer = inter(min_list, max_list, dimensions, query)
    return answer


def main():
    """Reading in file"""
    file_name = input("Enter name of file with extension: ")
    answer = data_gathering(file_name)
    print("Interpolated vector data: ", answer)


main()

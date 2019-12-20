# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# UIN:          528000393
# Name: 		Alex Tung
# Section:		552
# Assignment:	Lab 7B (e.g. Lab 1b-2)
# Date:		08 10 2019

from math import *
vectorA = []
vectorB = []
while True:
    dimA = int(input("How many dimensions of vector A(Enter 9999 to stop): "))
    if dimA == 9999:
        break
    vectorA.append(dimA)
    dimB = int(input("How many dimensions of vector B(Enter 9999 to stop): "))
    vectorB.append(dimB)
print("____________________________________")
print("Dimensions of vector A: ", vectorA)
print("Dimensions of vector B: ", vectorB)
print("____________________________________")

totalA = 0
totalB = 0
add = []
minus = []
totalAB = 0

for i in range(len(vectorA)):
    totalA += vectorA[i]**2
    totalB += vectorB[i]**2
    totalA = sqrt(totalA)
    totalB = sqrt(totalB)
    add.append(vectorA[i] + vectorB[i])
    minus.append(vectorA[i] - vectorB[i])
    totalAB += (vectorA[i]*vectorB[i])
print("Magnitude of vector A: ", totalA)
print("Magnitude of vector B: ", totalB)
print("____________________________________")
print("Vector A plus vector B equals:", add)
print("Vector A minus vector B equals:", minus)
print("____________________________________")
print("The dot product of vector A and B equals:", totalAB)

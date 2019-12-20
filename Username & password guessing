# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# UIN:          528000393
# Name: 		Alex Tung
# Section:		552
# Assignment:	Lab 7B (e.g. Lab 1b-2)
# Date:		08 10 2019

# Getting info for users/pass
num = int(input("Number of usernames/passwords: "))
info = {}
length = len(info)
length += num
counter = 0
while counter < num:
    user = str(input("Username: "))
    pas = str(input("Password: "))
    info[user] = pas
    print("_________________")
    counter += 1

# Guessing user/pass in 3 attempts
guesses = 1
while True:
    userX = str(input("Please enter username: "))
    pasX = str(input("Please enter password: "))
    if guesses < 3:
        if userX in info:
            if info[userX] == pasX:
                print("Login successful.")
                break
            else:
                print("Try again.")
                guesses += 1
        else:
            print("Please enter a valid username.")
    else:
        print("You have been locked out after 3 incorrect attempts.")
        break

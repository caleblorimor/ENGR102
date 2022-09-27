# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:        Caleb Lorimor
# Section:      565
# Assignment:   Lab 5.4
# Date:         26 September 2022

import math
# importing math
extemp = float(input("Enter the excess temperature: "))
if 1.3 <= extemp <= 5:
    y0 = 1000
    x0 = 1.3
    y1 = 7000
    x1 = 5
# the interval if statement is if the user inputs a quantity between 1.3 and 5
elif 5 <= extemp <= 30:
    y0 = 7000
    x0 = 5
    y1 = 1.5 * 10**6
    x1 = 30
# the interval if statement is if the user inputs a quantity between 5 and 30
elif 30 <= extemp <= 120:
    y0 = 1.5 * 10**6
    x0 = 30
    y1 = 2.5 * 10**4
    x1 = 120
# the interval if statement is if the user inputs a quantity between 30 and 120
elif 120 <= extemp <= 1200:
    y0 = 2.5 * 10**4
    x0 = 120
    y1 = 1.5 * 10**6
    x1 = 1200
# the interval if statement is if the user inputs a quantity between 120 and 1200
else:
    print("Surface heat flux is not available")
# the else statement if the user inputs anything above 1200 or below 1.3

m = (math.log(y1/y0))/(math.log(x1/x0))
y = round(y0*(extemp/x0)**m)
# creates equation for the slope and then puts the slope into y to calculate the heat flux
print(f"The surface heat flux is approximately {y} W/m^2")
# prints the surface heat flux

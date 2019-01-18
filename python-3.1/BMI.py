#BMI
#Austin Cefaratti 1/17/19
#calculates a persons BMI

import math

def main():
    weight = eval(input("Enter your weight in Pounds: "))
    print()
    height = eval(input("Enter your height in Inches: "))
        BMI = (weight * 720) / (height ** 2)
    if BMI > 25:
        print()
        print("Your BMI is: ", BMI)
        print()
        print("You are unhealthy.")
        print()
    elif BMI < 19:
        print()
        print("Your BMI is: ", BMI)
        print()
        print("You are unhealthy.")
        print()
    else:
        print()
        print("Your BMI is: ", BMI)
        print()
        print("You are healthy.")
        print()
main()

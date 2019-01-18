#Remakeing the program
#Austin Cefaratti 1/18/19
#Make a program into a sturdy program

import math

def main():
    a = 0
    while a == 0:
        try:
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
                a = a + 1
            elif BMI < 19:
                print()
                print("Your BMI is: ", BMI)
                print()
                print("You are unhealthy.")
                print()
                a = a + 1
            else:
                print()
                print("Your BMI is: ", BMI)
                print()
                print("You are healthy.")
                print()
                a = a + 1
        except:
            print()
            print("Unable to solve problem")
            print()
            print("Restarting Program")
            print()
main()

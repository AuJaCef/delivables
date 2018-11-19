#Distance seaker
#Austin C 11/5/18
#Tracks the distance between two points

import math

def main():
    print("This program finds the distance between two points")
    x1 = eval(input("What is the x corrordinate for one point: "))
    y1 = eval(input("What is the y corrordinate for the same point: "))
    x2 = eval(input("What is the x corrordinate for a diffrent point: "))
    y2 = eval(input("What is the y corrordinate for said point: "))

    D = math.sqrt(((x2 -x1) ** 2 + (y2 -y1) ** 2))
    print("The distance is about: ",D)
main()

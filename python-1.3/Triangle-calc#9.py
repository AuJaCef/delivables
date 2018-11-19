#Triangle
#Austin C 11/15/18
#checks length and area of a triangle

import math

def main():
    print("This checks the area and side length of a triangle")
    a = eval(input("What is the length of side 1: "))
    b = eval(input("What is the length of side 2: "))
    c = eval(input("What is the length of side 3: "))

    s = (a + b + c) / 2

    A = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("The side length of the triangle is: ",s)
    print("The area of the triangle is: ",A)
main()

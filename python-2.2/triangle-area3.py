#computes triangle
#Austin Cefaratti 1/16/19
#It computer the size of a triangle

import math

def size(a,b,c):
    S = (a + b + c) / 2
    return S
def area(S,a,b,c):
    Area = math.sqrt(S * (S - a) * (S - b) * (S - c))
    return Area
def main():
    print("This program calculates the area of a triangle.")
    a = eval(input("Enter side one: "))
    print()
    b = eval(input("Enter side two: "))
    print()
    c = eval(input("Enter side three: "))
    print()
    abc = size(a,b,c)
    print("The total length of the triangle is: ", abc)
    print()
    print("The area of the triangle is: ", area(abc,a,b,c))
    print()
    print("This code is copyrighted by the Combobert Corperration.")






main()




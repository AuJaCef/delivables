#ladder
#Austin C 11/15/18
#calculates the ladder

import math

def main():
    print("this program calculates the size of a ladder")
    h = float(input("What is the hight of the ladder: "))
    x = float(input("sin angle of ladder "))
    sin = math.radians(x)
    L = h / sin
    print("The length of the ladder is: " , L)
main()
    
    

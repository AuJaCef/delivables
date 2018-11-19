#Pi
#Austin C 11/15/18
#Does pie

import math

def main():
    print("Hello, user this program finds pi.")# print introduction

    n = eval(input("How many times would you like to loop: "))# gather input, save as n

    # assign variables: total for running total of pi, sgn for plus or minus
    total = 0.0
    sgn = 1.0

    # loop x by n times, but increment in odd numbers
    for x in range(1, n*2, 2):
        # formula to add 4/x to total
        total = total + sgn * 4.0/x
        # switch sgn to other side (-, +)
        sgn = -sgn
    # output total
    print("The total is: ", total)
    # output diff of pi and total
    total2 = total - math.pi
    print("The diffrence between ", total ," and Pi is: " ,total2)
        
    
main()

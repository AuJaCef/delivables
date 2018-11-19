#Challenge 2
#Austin C 11/19/18
#finds how long it will take to server people in line

import math

def main():
    p = eval(input("How many people are in line: "))

    Time = 4 * p

    print("It will take ", Time , " minutes in order to serve " , p , " people.")
main()

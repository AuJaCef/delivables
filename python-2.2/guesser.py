#Guesser
#Austin Cefaratti 1/16/19
#checks guess and sees how far off you were

import math
def true(x):
    c = math.sqrt(x)
    return c
def off(c,y):
    pre = c - y
    tru = abs(pre)
    return tru
def main():
    print("This program can help users guess a square root")
    x = eval(input("Enter a number to square root: "))
    y = eval(input("What do you think the square root will be: "))
    c = true(x)
    print()
    print("The square root was: ",c)
    print()
    print("You guessed: ", y)
    print()
    print("You were off by: " , off(c,y))
    print()
    print("This program was created and copyrighted by the Combobert Corperration.")
main()

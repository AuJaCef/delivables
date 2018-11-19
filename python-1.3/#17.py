#Guess
#Austin C 11/15/18
#checks and approves


import math

def main():
    print("This program can help users guess a square root")
    x = eval(input("Enter a number to square root: "))
    guess = eval(input("What do you think the square root will be: "))

    y = (( guess + (x/guess)) / 2)

    c = math.sqrt(x)

    pre = c - y

    tru = abs(pre)

    print("The square root was: " ,c)

    print("Your prediction was off by: ", tru)
    
main()

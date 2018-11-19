#Fibonacci
#Austin C 11/15/18
#does the Fibonacci sequence

import math

def main():
    print("This program will do the Fibonacci sequence up to a number")
    f = eval(input("What number do you want it to end at: "))

    done = f

    number1 = 0

    number2 = 1
    counter = 0

    if done <= 0:
        print("not possible")
    elif done == 1:
        print("It goes up to", done , ":")
        print(number1)
    else:
        print("It goes up to", done , ":")
    while counter < done:
        print(number1,end=' , ')
        numberth = number1 + number2
        number1 = number2
        number2 = numberth
        counter += 1


main()

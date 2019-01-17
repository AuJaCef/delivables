#Fibonacci number2
#Austin Cefaratti 1/16/19
#Does a Fibonacci number again

import math

def calc(f):
    number1 = 0
    number2 = 1
    counter = 0
    if f <= 0:
        print("Impossible to do.")
    elif f == 1:
        print("It goes up to", f , ":")
        print(number1)
    else:
        print("It goes up to", f , ":")
    while counter < f:
        print(number1,end=' , ')
        numberth = number1 + number2
        number1 = number2
        number2 = numberth
        counter += 1
def main():
    print("This program does a fibonacci sequence.")
    f = eval(input("What number do you want to end at: "))
    print()
    calc(f)
    print()
    print("This code was made and copyrighted by the Combobert Corperration.")
main()

    

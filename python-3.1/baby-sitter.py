#Baby sitter
#Austin Cefaratti 1/17/19
#finds the amount the sitter earns

import math

def main():
    print("The hours will be bassed off of military time")
    print()
    start = eval(input("Enter the time when the sitting started: "))
    print()
    end = eval(input("Enter the time when the sitting ends: "))
    if end > 21:
        sleeptime = end - 21
        aftersleep = sleeptime * 1.75
        beforesleep = (21 - start) * 2.50
        money = aftersleep + beforesleep
        print()
        print("The baby sitter earned: ",money," dollars.")
        print()
    elif start >= 21:
        money = (end - start) * 1.75
        print()
        print("The baby sitter earned: ",money," dollars.")
        print()
    else:
        money = (end - start) * 2.50
        print()
        print("The baby sitter earned: ",money," dollars.")
        print()
    



main()

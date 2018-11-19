#Challenge 3
#Austin C 11/19/18
#Finds cost for bikes and helmets

import math

def main():
    h = eval(input("How many helments did you sell in one month: "))
    b = h * 5
    bp = b * 250
    hp = h * 50
    total = hp + bp

    print("The shop got: ", total ," dollars from " , b ," bikes and ", h , " helmets.")


main()

#Challenge 5
#Austin C 11/19/18
#gives change (money)

import math

def main():
    print("This is a change counter")
    coins = eval(input("How much cents do you have (0 - 99): "))
    print(coins//25, "Quarters")
    coins = coins%25
    print(coins//10, "Dimes")
    coins = coins%10
    print(coins//5, "Nickles")
    coins = coins%5
    print(coins//1, "Pennies")
main()

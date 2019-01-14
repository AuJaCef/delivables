#Updated change counter
#Austin Cefaratti 1/3/19
#counts change, but advanced

import time

def main():
    print("This is a change counter\n")
    coins = eval(input("How many cents do you have(0 - 99): "))
    print("\n")
    time.sleep(0.5)
    print(coins//25, "Quarters")
    coins = coins%25
    print("\n")
    time.sleep(0.5)
    print(coins//10, "Dimes")
    coins = coins%10
    print("\n")
    time.sleep(0.5)
    print(coins//5, "Nickles")
    coins = coins%5
    print("\n")
    time.sleep(0.5)
    print(coins//1, "Pennies")
    print("\n")
    print("Thank you user for using this program.")
main()

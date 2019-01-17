#sum list
#Austin Cefaratti
#adds a value to all items is a list

import math

def sumList(nums):
    return [i + 5 for i in nums]
def main():
    print("This program adds 5 a list of numbers")
    nums = [1,2,3,4,5,6,7,8]
    print()
    print("the original numbers are: ",nums)
    print()
    print("The new numbers are: ",sumList(nums))
    print()
    print("Created and owned by the Combobert Corperration")
main()

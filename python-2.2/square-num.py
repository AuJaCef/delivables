#square each
#Austin Cefaratti 1/16/19
#squares each number

import math

def squareEach(nums):
    return [i ** 2 for i in nums]
def main():
    print("This program squares a list of numbers")
    nums = [1,2,3,4,5,6,7,8]
    print()
    print(squareEach(nums))
    print()
    print("Created and owned by the Combobert Corperration")
    
    


main()

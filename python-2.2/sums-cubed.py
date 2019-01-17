#natural
#Austin Cefaratti 1/15/18
#cubes a number asked for

def sumN(n):
    sums = n + n
    #print("The sum of the number given is: ",sums)
    return sums
def sumNCubes(sums):
    cubes = sums * sums * sums
    #print("The cubed sume of the number given is: ",cubes)
    return cubes
def main():
    print("This program asks for a number and gives both the sum and the cubed of the sum.")
    n = eval(input("Enter a natural number: "))
    print()
    #sumN(n)
    n = sumN(n)
    print(n)
    print()
    print(sumNCubes(n))
    print()
    print("The wonderful star, Combobert Technitional helped")
    print("several programers make this program work.")
main()

#multi-math
#Austin Cefaratti 1/16/19
#find the square of a sum of the lines in a code

def cubeN(lines):
    lines = lines ** 2
    return lines
def numsN(lines):
    linesSP = lines + 5
    return linesSP
def main():
    print("Finds the sum of a cubed based on the amount of line of code(added by 5)")
    print()
    file = input("Enter a file: ")
    lines = len(open(file).readlines( ))
    print()
    print("The amount of lines in that file is: ",lines)
    print()
    lines = cubeN(lines)
    print("The value at the end is: ",numsN(lines))
    print()
    print("Created and owned by the Combobert Corperration")
main()

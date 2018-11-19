#atom
#Austin c 11/15/18
#checks atom diffrence

def main():
    print("This program checks the weight of a carbohydrate")
    H = eval(input("How many hydrogen particles are there: "))
    C = eval(input("How many carbon particles are there: "))
    O = eval(input("How many oxygen particles are there: "))

    Ca = (H * 1.00794) + (C * 12.0107) + (O * 15.9994) #inputs the equation to find the weight of the carbohydrate

    print("The total weight of the carbohydrate is: " ,Ca)
main()

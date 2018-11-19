#natural number
#Austin C 11/15/18
#finds the sum of the cubed first natural number

def main():
    print("This makes a natural number cubed")
    n = eval(input("Enter a natural number: "))

    n2 = n + 1

    a = range(n2)

    b = sum(a) ** 3 

    print("The cubed natural number is: " ,b)
main()


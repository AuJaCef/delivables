#natural number
#Austin C 11/15/18
#finds the sum of the first natural number

def main():
    print("This makes a sum of a natural number")
    n = eval(input("Enter a natural number: "))

    n2 = n + 1

    a = range(n2)

    b = sum(a)

    print("The sum of the natural number is: " ,b)
main()

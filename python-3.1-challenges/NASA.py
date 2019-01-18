#Nasa
#Austin Cefaratti 1/18/19
#Does a compution based of how many numbers are the same

def main():
    a = eval(input("Enter the first number: "))
    b = eval(input("Enter the second number: "))
    c = eval(input("Enter the third number: "))

    if a == b:
        if b == c:
            print(a)
        else:
            print(a)
    elif b == c:
        if c == a:
            print(b)
        else:
            print(b)
    elif c == a:
        if a == b:
            print(c)
        else:
            print(c)
    else:
        for i in range(5):
            print()
            print("ERROR")
            print()
main()

#Chaos...again
#Austin Cefaratti 1/3/18
#Does a chaos program

def main():
    b = 0
    e = 0
    print("this program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter a second number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    print("-------------------------")
    print(x)
    print("-------------------------")
    for i in range(n) :
        x = 3.9 * (x - x * x)
        e = e + 1
        print(e , ". ", x)
    print("-------------------------")
    print(y)
    print("-------------------------")
    for q in range(n):
        y = 3.9 * (y - y * y)
        b = b + 1
        print(b , ". ", y)
main()

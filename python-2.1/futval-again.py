#futval again
#Austin Cefaratti
#Finds the future value of your money

def main():
    print("this program cqalculates the amount of investment you have after a set amount of years")
    c = 0
    principal = eval(input("enter the amount you would like to invest: "))
    apr = eval(input("Enter you intrest rate: "))
    year = eval(input("how long would you like to invest: "))
    print("Year | Value")
    print("------------------")
    print(c,". |$", principal)
    for i in range(year) :
        principal = round(principal * (1 + apr),2)
        c = c + 1
        print(c,". |$",principal)
main()

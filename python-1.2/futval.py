#futval
#Austin C 11/14/18
#year calculator?

def main():
    print("this program cqalculates the amount of investment you have after a set amount of years")

    x = eval(input("enter the amount you would like to invest: "))
    y = eval(input("Enter you intrest rate: "))
    n = eval(input("how long would you like to invest: "))
    for i in range(n) :
        x = x * (1 + y)
    print("The amount of investment after said amount of years should be: ", x)
main()    

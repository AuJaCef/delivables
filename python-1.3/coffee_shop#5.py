#coffee
#Austin C 11/15/18
#checks cost

def main():
    x = eval(input("How many pounds is the coffee: "))

    c = (10.50 * x) + (0.86 * x) + 1.50

    print("The cost for coffee in dollars is: ", c)
main()

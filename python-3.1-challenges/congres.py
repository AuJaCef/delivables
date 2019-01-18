#congress
#Austin Cefaratti 1/18/19
#Sees if a vote has passed


def main():
    choose = eval(input("Which house is voting(1 is Representatives, 2 is Senate): "))
    if choose == 1:
        print()
        yea = eval(input("How many people said yes to the vote in Rep.: "))
        if yea > 217.5:
            print()
            print("The vote has passed.")
            print()
        else:
            print()
            print("The vote did not pass passed.")
            print()
    elif choose == 2:
        print()
        yea1 = eval(input("How many people said yes to the vote in Rep.: "))
        if yea1 > 50:
            print()
            print("The vote has passed.")
            print()
        elif yea1 == 50:
            print()
            print("The vote was tied.")
            print()
        else:
            print()
            print("The vote did not pass passed.")
            print()
    else:
        print()
        print("That is not a valid input")
        print()
main()

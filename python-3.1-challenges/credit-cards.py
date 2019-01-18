#creditcards
#Austin Cefaratti 1/18/19
#Finds out what credit card you are using

def main():
    cred = eval(input("Enter your credit card number(16 didgets): "))

    if cred > 6999999999999999:
        print()
        print("Unknown credit card")
        print()
    elif cred >= 6000000000000000:
        print()
        print("It is a Discover credit card")
        print()
    elif cred >= 5000000000000000:
        print()
        print("It is a Master card")
        print()
    elif cred >= 4000000000000000:
        print()
        print("It is a Visa credit card")
        print()
    else:
        print()
        print("Unknown credit card")
        print()
main()

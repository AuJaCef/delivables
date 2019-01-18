#Password check
#Austin Cefaratti 1/18/19
#Checks to see if you have a strong password


def main():
    password = input("What is your password: ")
    password = len(password)
    if password > 12:
        print()
        print("You have a very strong Password")
        print()
    elif password >= 8:
        print()
        print("You have a moderately strong Password")
        print()
    else:
        print()
        print("You have a weak password")
        print()
main()

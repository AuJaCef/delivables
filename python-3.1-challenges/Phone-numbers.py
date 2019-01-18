#Phone Numbers
#Austin Cefaratti 1/18/19
#Checks if the number is valid

def main():
    phonenum = input("Enter a phone number: " )
    phonenum = len(phonenum) - phonenum.count('-')
    if phonenum == 10:
        print()
        print("This phone number is valid")
        print()
    else:
        print()
        print("This phone number isn't valid")
        print()


main()

#valid date
#Austin Cefaratti 1/17/19
#Checks if the date is valid

def main():
    month = eval(input("What month of the year is it: "))
    print()
    day = eval(input("What day of the month is it: "))
    print()
    year = eval(input("What year is it: "))
    year1 = year % 4

    if month > 12:
        print()
        print("The date isn't valid")
        print()
    elif day > 32:
        print()
        print("The date isn't valid")
        print()

    elif year1 > 0:
        if month == 2:
            if day > 28:
                print()
                print("The date isn't valid")
                print()
            else:
                print()
                print("The date is valid")
                print()
    elif year1 == 0:
        if month == 2:
            if day >= 30:
                print()
                print("The date isn't valid")
                print()
            else:
                print()
                print("The date is valid")
                print()
        elif month == 4 or month == 6 or month == 9 or month ==11:
            if day > 30:
                print()
                print("The date isn't valid")
                print()
            else:
                print()
                print("The date is valid")
                print()
        else:
            print()
            print("The date isn't valid")
            print()
    elif month == 0:
        print()
        print("The date isn't valid")
        print()
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            print()
            print("The date isn't valid")
            print()
        else:
            print()
            print("The date is valid")
            print()
    else:
        print()
        print("The date is valid")
        print()
main()

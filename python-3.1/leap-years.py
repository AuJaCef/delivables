#Leap years
#Austin Cefaratti 1/17/19
#Finds what years are leap years

def main():
    year = eval(input("What year is it: "))
    year1 = year % 4
    if year1 == 0:
        print()
        print("The year of ",year," is a leap year")
        print()
    else:
        print()
        print("The year of ",year," is not a leap year")
        print()
main()

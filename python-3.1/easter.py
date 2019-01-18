#Easter
#Austin Cefaratti 1/17/19
#Finds the date of easter

def main():
    year = eval(input("What year is it: "))
    a = year % 19 
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    easter = 22 + d + e
    if easter >= 32:
        easter = easter - 31
        print()
        print("Easter is on April ",easter," on the year of ",year)
        print()
    else:
        print()
        print("Easter is on March ",easter," on the year of ",year)
        print()
main()

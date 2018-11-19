#Moon
#Austin C 11/15/18
#Find the Gregorian epact

def main():
    print("This program finds how many days it has been sience the last new moon after new years")
    year = eval(input("What year is it: "))
    C = year//100

    epact = (8 + (C // 4) - C + ((8 * C + 13)//25) + 11 * (year % 19)) % 30

    print("The epact is: ", epact)
main()

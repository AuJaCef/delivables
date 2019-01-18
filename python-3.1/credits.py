#credits
#Austin Cefaratti 1/17/19
#Sees where your class standing is

def main():
    credit = eval(input("How many credits do you have: "))
    if credit >= 26:
        print()
        print("You are in Senior year")
        print()
    elif credit >= 16:
        print()
        print("You are in Junior year")
        print()
    elif credit >= 7:
        print()
        print("You are in Sophomore year")
        print()
    else:
        print()
        print("You are in Freshman year")
        print()

main()

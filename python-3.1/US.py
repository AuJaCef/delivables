#US senator
#Austin Cefaratti 1/17/19
#Find is they are eligable for politics


def main():
    age = eval(input("How old are you: "))
    print()
    time = eval(input("How long were you a US citizen: "))
    print()
    if age >= 30:
        if time >= 9:
            print("You can be a US senator or a representative")
        elif time >= 7:
            print("You can be a US representative")
        else:
            print("You have not been a US citizen long enough")
    elif age >= 25:
        if time >= 7:
            print("You can be a US representative")
        else:
            print("You have not been a US citizen long enough")
    else:
        print("You are not old enough to be a US senator or a representative")
main()

#quiz 1
#Austin Cefaratti 1/17/19
#Grades a quiz


def main():
    score = eval(input("enter a score between 5-0: "))
    if score >= 5:
        print("This studen got an A")
    elif score == 4:
        print("This student got a B")
    elif score == 3:
        print("This student got a C")
    elif score == 2:
        print("This student got a D")
    else:
        print("This student got a F")


main()

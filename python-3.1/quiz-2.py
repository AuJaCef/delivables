#quiz 2
#Austin Cefaratti 1/17/19
#Grades a quiz


def main():
    score = eval(input("enter a score between 100-0: "))
    if score >= 90:
        print("This studen got an A")
    elif score >= 80:
        print("This student got a B")
    elif score >= 70:
        print("This student got a C")
    elif score >= 60:
        print("This student got a D")
    else:
        print("This student got a F")

main()

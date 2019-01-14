#score reader plus
#Austin Cefaratti 12/14/18
#Reads score on a 0 - 100 basis

def main():
    scores = eval(input("Enter the scores (0 - 100): "))

    if scores >= 90:
        print("The grade for the test is an A")
    elif scores >= 80:
        print("The grade for the test is a B")
    elif scores >= 70:
        print("The grade for the test is a C")
    elif scores >= 60:
        print("The grade for the test is a D")
    else:
        print("The grade for the test is a F")

main()

#letter grade 2
#Austijn Cefaratti 1/16/19
#gives you a letter grade

def scores(s):
    if s >= 90:
        print("The grade for the test is a A.")
    elif s >= 80:
        print("The grade for the test is a B.")
    elif s >= 70:
        print("The grade for the test is a C.")
    elif s >= 60:
        print("The grade for the test is a D.")
    else:
        print("The grade for the test is a F.")
def main():
    print("This program gives a score based on the number entered")
    print()
    s = eval(input("Enter a score between 0 and 100: "))
    print()
    scores(s)
    print()
    print("This program was created and copyrighted by the Combobert Corperration")
main()    

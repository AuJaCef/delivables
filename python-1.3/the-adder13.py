#sumer
#Austin C 11/15/18
#collects numbers inserted by the user and adds them

def main():
    print("enter numbers into this program will add them up")
    l = float(input("how many numbers do you want to add: "))
    for i in range(l):
        x = 0
        a = eval(input("Enter your number: "))
        x = a + x
    print("The sum is: ",x)
main()

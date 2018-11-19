#Averager
#Austin C 11/15/18
#Finds the average

def main():
    whole = 0
    rep = eval(input("How many numbers: "))

    for i in range(rep):
        num = eval(input("Enter a number: "))
        whole = whole + num
    average = whole / rep
    print("The average is: ",average)
main()

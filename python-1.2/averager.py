#averager
#Austin C 11/14/18
#calculates the average

def main():
    print("this program finds the average of scores")
    x = eval(input("enter the first test score 0-100: "))
    y = eval(input("enter the second test score 0-100: "))
    z = eval(input("enter the third test score 0-100: "))
    a = (x + y + z) / 3
    print(a)
main()

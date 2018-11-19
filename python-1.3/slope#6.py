#Slope
#Austin C 11/15/18
#Finds the slope

def main():
    print("This program finds the slope between two points")
    x1 = eval(input("What is the x corrordinate of one point: "))
    y1 = eval(input("What is the y corrordinate of the same point: "))
    x2 = eval(input("What is the x corrordinate of the other point: "))
    y2 = eval(input("What is the y corrordinate of the said point: "))

    y3 = y2 - y1
    x3 = x2 - x1

    s = y3 / x3

    print("The slope is: " ,s)
main()

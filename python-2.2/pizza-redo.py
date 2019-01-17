#pizza redo
#Austin Cefaratti 1/15/19
#does the pizza question again, but better


def sizecR(r):
    area = 3.14 * (r * r)
    return area
def sizecRA(area):
    RA = area * 0.13
    return RA
def main():
    print("This program calculates the size and price of a pizza")
    print()
    print("Enter a radius for how big do you want the pizza to be")
    r = eval(input("Enter the radius (1 inch of area is $0.03): "))
    print()
    print("the size of the pizza is")
    r = sizecR(r)
    print(r)
    print()
    print("The cost for your pizza is")
    print("$" + str(round(sizecRA(r), 2)))
    print()
    print("This program was made by Combobert Technitional,")
    print("you can see it in his new store Combobert Pizza's")
main()

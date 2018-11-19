#Volume calculator
#Austin C 11/15/18
#calculates the volume of a sphere

def main():
    r = eval(input("What is the radius of the sphere: " ))
    V = 4/3 * 3.14 * ( r ** r * r)
    print("The volume of the sphere is: " ,V)
main()

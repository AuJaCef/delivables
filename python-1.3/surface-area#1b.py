#Surface area
#Austin 11/15/18
#finds the surface area of a sphere

def main():
    print("This calculates the surface area of a sphere")
    r = eval(input("Enter the radius of the sphere: "))
    A = 4 * 3.14 * (r ** r)
    print("The surface area is: " ,A)
main()

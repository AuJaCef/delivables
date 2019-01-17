#give functions
#Austin Cefaratti 1/15/19
#gioves functions definitions


def sphereArea(r):
    Area = 4 * 3.14 * (r * r)
    print("The area is about: " ,Area)
def sphereVolume(r):
    Volume = (4 / 3) * 3.14 * (r * r * r)
    print("The volume is about: " ,Volume)
def main():
    print("This program asks the user for radius and gives both area")
    print("and volume of the sphere.")
    print()
    r = eval(input("What is the radius of the sphere: " ))
    print()
    sphereArea(r)
    print()
    sphereVolume(r)
    print()
    print("The upcoming computer singing star has helped")
    print("make this program for all to use.")
main()

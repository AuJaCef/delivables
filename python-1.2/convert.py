#convert
#Austin C 11/14/18
#it converts?

def main():
    print("Hello, user")
    ("Press the <Enter> ket to quit.")
    for i in range(5):
        #this will loop
        x = eval(input("Enter the tempeture outside in farenheit: "))
        print("----------------------------------------")
        print (x)
        print("farenheit")
        print("----------------------------------------")
        y = 5/9 * (x - 32)
        print(y)
        print("celsius")
        print("----------------------------------------")
        #until the end of the indented section
main()

#math
#Austin C 11/13/18
# does math

def main():
    print("this program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range(n) :
        x = 3.9 * (x - x * x)
        print(x)
main()
        

#numeric value +
#Austin Cefaratti 1/2/19
#Does really long names

def main():
    sums = 0
    nameStr = input("Enter a name: ")
    for c in nameStr:
        sums += ord(c.lower()) - ord("a") + 1
    print(sums)
    
main()

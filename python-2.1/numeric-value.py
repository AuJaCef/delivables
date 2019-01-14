#numeric value of a name
#Austin Cefaratti 1/2/19
#Finds the numeric value of a name

def main():
    sums = 0
    nameStr = input("Enter a name: ")
    for c in nameStr:
        sums += ord(c.lower()) - ord("a") + 1
    print(sums)
    
main()

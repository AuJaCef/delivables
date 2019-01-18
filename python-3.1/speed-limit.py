#Speed limit
#Austin Cefaratti 1/16/19
#finds the speeding fee

def main():
    limit = eval(input("What is the speed limit: "))
    print()
    speed = eval(input("How fast was the driver going: "))
    if speed > 90:
        fine = 200 + (50 + ((speed - limit) * 5))
        print()
        print("You are fined: ",fine)
        print()
    elif speed > limit:
        fine = 50 + (speed - limit) * 5
        print()
        print("You are fined: ",fine)
        print()
    else:
        print()
        print("You are not fined anything.")
        print()
main()    

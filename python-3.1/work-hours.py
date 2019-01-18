#work hours
#Austin Cefaratti 1/17/19
#Finds the hourly rate

def main():
    h = eval(input("Enter the amount of hours you worked this week: "))
    hw = eval(input("Enter your hourly wage: "))
    if h > 40:
        m = (hw * 1.5) * h
    else:
        m = hw * h
    print("You got ",m,"dollars this week")
main()

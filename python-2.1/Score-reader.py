#Scroe reader
#Austin Cefaratti 12/14/18
#reads scores


def main():
    scores = input("Enter the scores (0 - 5): ")

    scoreStr = scores

    grade = ["F", "F", "D", "C", "B", "A"]

    scoreStr = grade[int(scoreStr)]
    
    print("The grade for the test is: ", scoreStr)

main()

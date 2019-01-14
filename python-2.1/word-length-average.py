#Word length average
#Austin Cefaratti 1/3/19
#This find the average length of the words in a sentence

def main():
    print("This program finds the average amount ofletters per word.")
    text = input("Enter a sentence or two: ")
    text2 = text.split()
    wordcount = len(text2)
    print("The total word count for this text is: " ,wordcount)

    lettercount = len(text)

    lettercount = len(text) - text.count(' ')

    print("The letter count for the text without spaces is: " ,lettercount)

    average = round(lettercount / wordcount)

    print("The average amount of letters per words without spaces is about : " ,average)
main()

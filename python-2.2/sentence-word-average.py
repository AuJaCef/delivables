#sentence, word average 2
#Austin Cefaratti 1/16/19
#Find the average length of the words in a sentence but again

def length(text):
    text2 = text.split()
    wordcount = len(text2)
    print("The total word count for this text is: " ,wordcount)
    return wordcount
def length2(text):
    lettercount = len(text)
    lettercount = len(text) - text.count(' ')
    print("The letter count for the text without spaces is: " ,lettercount)
    return lettercount
def length3(wordcount,lettercount):
    average = round(lettercount / wordcount)
    print("The average amount of letters per words without spaces is about : " ,average)
    return average
def main():
    print("This program finds the average amount ofletters per word.")
    print()
    text = input("Enter a sentence or two: ")
    print()
    wordcount = length(text)
    print()
    lettercount = length2(text)
    print()
    length3(wordcount,lettercount)
    print()
    print("This program was created and copyrighted by the Combobert Corperration")
main()

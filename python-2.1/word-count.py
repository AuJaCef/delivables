#Word counter
#Austin Cefaratti 1/3/18
#Counts the words in a sentance

def main():
    print("This program counts the amount of words in a sentence.")
    #Gets the sentence from the user
    text = input("Please enter your sentence here, user: ")
    text2 = text.split()
    wordamount = len(text2)
    #This outputs the number of words in one sentence
    print("The total amount of words in this sentence is: " ,wordamount)
main()

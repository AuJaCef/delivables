#Acronym
#Austin Cefaratti 12/14/18
#makes acronyms

def main():
    acrStr = input("Enter three words(place / beteween them): ")

    word1Str, word2Str, word3Str = acrStr.split("/")

    word1Str = word1Str.upper()[0]

    word2Str = word2Str.upper()[0]

    word3Str = word3Str.upper()[0]
    print("The acronym is: " ,word1Str + word2Str + word3Str)
main()

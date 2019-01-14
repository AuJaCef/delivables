#Numeric value extra plus
#Austin Cefaratti
#A even better version of numeric value

import math

def main():
    output = ""
    word = input("Enter a word: ").lower()
    key = int(input("Enter the amount of change you wish: "))    
    chars = "abcdefghijklmnopqrstuvwxyz"
    for i in word:
        pos = chars.find(i)
        newpos = (pos + key) % len(chars)
        output += str(newpos)
    print(output)
    print("Converting back to original")
    print(word)
    #for i in newpos:
    #    word = pos.find(i)
    #    oldpos = (word - key) % len(chars)
    #    print(oldpos)
main()

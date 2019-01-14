#Word count python
#Austin Cefaratti 1/4/18
#Gets the amount of words in a file

import os
import collections
import pprint

def main():

    file = input("Enter a file path: ")
    counter = len(open(file).readlines( ))
    numw = 0

    with open(file, 'r') as f:
        for line in f:
            words = line.split()
            numw += len(words)          
    with open(file, 'r') as info:
        count = collections.Counter(info.read().upper())
        char_num = pprint.pformat(count)     
    print("Number of Characters", char_num)
    print("Number of words: ", numw)
    print("Number of lines: ", counter)
main()

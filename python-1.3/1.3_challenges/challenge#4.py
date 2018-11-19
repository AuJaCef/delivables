#Challenges
#Austin C 11/19/18
#Attemps to solve the wheat and chessboard problem

import math

def main():
    grain = 0
    print("This program attemps to solve the wheat and chessboard problem")
    for x in range(0, 64):
        grain = grain + 2 ** x
        
    print("The total amount of wheat on the chess board is: ", grain)
main()

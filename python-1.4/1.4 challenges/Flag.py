#Flag
#Austin Cefaratti 12/10/18
#Draws a flag

from graphics import *

def main():
    win = GraphWin("Italian flag", 330, 250)
    rect = Rectangle(Point(0,0), Point(110,250))
    rect.setFill("green")
    rect.draw(win)

    rect = Rectangle(Point(110,0), Point(220,250))
    rect.setFill("white")
    rect.draw(win)

    rect = Rectangle(Point(220,0), Point(330,250))
    rect.setFill("red")
    rect.draw(win)




main()

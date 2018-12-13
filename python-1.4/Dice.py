#Dice
#Austin Cefaratti 11/20/18
#draws dice

from graphics import *

def main():
    win = GraphWin("dice", 280, 80)
    rect = Rectangle(Point(20,20), Point(60,60))
    rect.setOutline("black")
    rect.setFill("white")
    rect.draw(win)

    rect = Rectangle(Point(70,20), Point(110,60))
    rect.setOutline("black")
    rect.setFill("white")
    rect.draw(win)

    rect = Rectangle(Point(120,20), Point(160,60))
    rect.setOutline("black")
    rect.setFill("white")
    rect.draw(win)

    rect = Rectangle(Point(170,20), Point(210,60))
    rect.setOutline("black")
    rect.setFill("white")
    rect.draw(win)

    rect = Rectangle(Point(220,20), Point(260,60))
    rect.setOutline("black")
    rect.setFill("white")
    rect.draw(win)

    #die 1
    center = Point(40,40)
    circ = Circle(center, 2)
    circ.setFill('black')
    circ.draw(win)
    
    #die 2
    center = Point(80,30)
    circ = Circle(center, 2)
    circ.setFill('black')
    circ.draw(win)

    center = Point(100,50)
    circ = Circle(center, 2)
    circ.setFill('black')
    circ.draw(win)

    #die 3
    center = Point(130,30)
    circ = Circle(center, 2)
    circ.setFill('black')
    circ.draw(win)
    
    center = Point(140,40)
    circ = Circle(center, 2)
    circ.setFill('black')
    circ.draw(win)

    center = Point(150,50)
    circ = Circle(center, 2)
    circ.setFill('black')
    circ.draw(win)

    #die 4
    center = Point(180,30)
    circ = Circle(center, 2)
    circ.setFill('black')
    circ.draw(win)

    center = Point(200,50)
    circ = Circle(center, 2)
    circ.setFill('black')
    circ.draw(win)

    center = Point(180,50)
    circ = Circle(center, 2)
    circ.setFill('black')
    circ.draw(win)

    center = Point(200,30)
    circ = Circle(center, 2)
    circ.setFill('black')
    circ.draw(win)

    #die 5
    center = Point(250,50)
    circ = Circle(center, 2)
    circ.setFill('black')
    circ.draw(win)

    center = Point(250,30)
    circ = Circle(center, 2)
    circ.setFill('black')
    circ.draw(win)

    center = Point(240,40)
    circ = Circle(center, 2)
    circ.setFill('black')
    circ.draw(win)

    center = Point(230,30)
    circ = Circle(center, 2)
    circ.setFill('black')
    circ.draw(win)

    center = Point(230,50)
    circ = Circle(center, 2)
    circ.setFill('black')
    circ.draw(win)
    
main()

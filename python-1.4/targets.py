#Targets
#Austin C 11/20/18
#Makes targets

from graphics import *

def main():
    win = GraphWin()
    center = Point(100, 100)
    circ = Circle(center, 50)
    circ.setFill('white')
    circ.draw(win)
    
    center = Point(100, 100)
    circ = Circle(center, 40)
    circ.setFill('black')
    circ.draw(win)
    
    center = Point(100, 100)
    circ = Circle(center, 30)
    circ.setFill('blue')
    circ.draw(win)
    
    center = Point(100, 100)
    circ = Circle(center, 20)
    circ.setFill('red')
    circ.draw(win)
    
    center = Point(100, 100)
    circ = Circle(center, 10)
    circ.setFill('yellow')
    circ.draw(win)
main()

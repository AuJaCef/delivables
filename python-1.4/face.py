#Face
#Austin C
#Makes a face

from graphics import *

def main():
    win = GraphWin()
    center = Point(100, 100)
    circ = Circle(center, 80)
    circ.setFill(color_rgb(255,187,133))
    circ.draw(win)

    center = Point(55, 80)
    circ = Circle(center, 15)
    circ.setFill(color_rgb(75, 36, 15))
    circ.draw(win)

    center = Point(55, 85)
    circ = Circle(center, 15)
    circ.setFill('white')
    circ.draw(win)

    center = Point(55, 85)
    circ = Circle(center, 5)
    circ.setFill('black')
    circ.draw(win)

    center = Point(155, 80)
    circ = Circle(center, 15)
    circ.setFill(color_rgb(75, 36, 15))
    circ.draw(win)

    center = Point(155, 85)
    circ = Circle(center, 15)
    circ.setFill('white')
    circ.draw(win)

    center = Point(155, 85)
    circ = Circle(center, 5)
    circ.setFill('black')
    circ.draw(win)

    center = Point(105, 110)
    circ = Circle(center, 15)
    circ.setFill(color_rgb(255,187,133))
    circ.draw(win)

    center = Point(105, 150)
    circ = Circle(center, 15)
    circ.setFill('black')
    circ.draw(win)
    
main()

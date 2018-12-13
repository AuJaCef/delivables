#line-seg
#Austin Cefaratti 12/10/18
#lets user draw a line segment

import math

from graphics import *

def main():
    win = GraphWin("LINES", 300, 300)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on two points" )
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    line = Line(p1, p2)
    line.setFill("blue")
    line.draw(win)

    a = line.getP1()

    b = line.getP2()

    print(a)

    print(b)

    dx = b.getX() - a.getX()
    dy = b.getY() - a.getY()

    slope = abs(dy/dx)

    print("The slope of your line is: " ,slope)

    length = math.sqrt((dx**2) + (dy**2))

    print("The length of your line is: " ,length)

    px = (b.getX() + a.getX())/2

    py = (b.getY() + a.getY())/2

    center = Point(px, py)
    circ = Circle(center, 0.2)
    circ.setFill('cyan')
    circ.draw(win)
    
    print("The midpoint is: " ,center)
    
    

    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()



main()

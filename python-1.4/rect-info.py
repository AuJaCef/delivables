#Rectangle info
#Austin Cefaratti 12/10/18
#Shows info about a rectangle drawn by the user

import math

from graphics import *

def main():
    win = GraphWin("Box", 300, 300)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on two points" )
    message.draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    rect = Rectangle(p1,p2)
    rect.draw(win)

    a = rect.getP1()

    b = rect.getP2()

    print(a)

    print(b)

    dx = b.getX() - a.getX()
    dy = b.getY() - a.getY()


    print(dy)

    print(dx)

    length = abs(dy)

    width = abs(dx)

    area = length * width

    peri = 2*(length + width)

    print("The area of your rectangle is: " ,area)

    print("The perimiter of your rectangle is: " ,peri)

    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()    

main()

#Triangle info
#Austin Cefaratti 12/10/18
#Informks the user about the triangle drawn

from graphics import *

import math

def main():
    win = GraphWin("Triangle", 300, 300)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points" )
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    tri = Polygon(p1, p2, p3)
    tri.draw(win)

    pointList = tri.getPoints()

    print(pointList)

    a = pointList[0].getX()

    a2 = pointList[1].getX()

    a3 = pointList[2].getX()

    b = pointList[0].getY()

    b2 = pointList[1].getY()

    b3 = pointList[2].getY()
    
    print(a)

    print(a2)

    print(a3)

    print(b)

    print(b2)

    print(b3)

    dx1 = a3 - a2

    dx2 = a2 - a

    dx3 = a3 - a

    
    dy1 = b3 - b2

    dy2 = b2 - b

    dy3 = b3 - b


    sidea = math.sqrt((dx1**2) + (dy1**2))

    sideb = math.sqrt((dx2**2) + (dy2**2))

    sidec = math.sqrt((dx3**2) + (dy3**2))

    s = (sidea + sideb + sidec)/2

    area = math.sqrt(s*(s - sidea)*(s - sideb)*(s - sidec))

    print("The side is about: ", s)

    print("The area is: ",area) 

    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

main()

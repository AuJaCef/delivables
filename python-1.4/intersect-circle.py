#intercector
#AustinCefaratti 12/10/18
#computer the intercection of a circle

import math

from graphics import *

def main():
    
    win2 = GraphWin("radius", 200,200)
    Text(Point(75, 150), "Enter radius: ").draw(win2)
    Text(Point(60, 100), "Enter y-intersect: ").draw(win2)
    r = Entry(Point(175, 150), 10).draw(win2)
    y = Entry(Point(175, 100), 10).draw(win2)
    Text(Point(100, 10), "Click to exit").draw(win2)
    win2.getMouse()
    ra = r.getText()
    ra = eval(ra)
    ya = y.getText()
    ya = eval(ya)
    win2.close()
    
    win = GraphWin("circle", 300,300)
    win.setCoords(-10,-10,10,10)
    center = Point(0,0)
    circ = Circle(center, ra)
    circ.setFill("blue")
    circ.draw(win)

    line = Line(Point(-100, ya), Point (100, ya))
    line.setFill("red")
    line.draw(win)


    x = abs(math.sqrt((ra ** 2) - (ya ** 2)))

    xa = x *- 1

    print("X values of intercation are: ", x ," and: ", xa )

main()

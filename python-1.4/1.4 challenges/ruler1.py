#Ruler
#Austin Cefaratti 12/10/18
#Draws a ruler

from graphics import *

def main():
    win = GraphWin("Ruler", 1160,100)
    point = Point(575,50)
    point.draw(win)

    #This makes the wood of the ruler

    rect = Rectangle(Point(0,10),Point(1160,90))
    rect.setFill("brown")
    rect.draw(win)

    #This massive wall of code makes the markes on the ruler
    #inch 0
    line = Line(Point(0.8,20), Point(0.8,40))
    line.draw(win)

    line = Line(Point(23.9575,35), Point(23.9575,40))
    line.draw(win)

    message = Text(Point(23.9575,25),"Inches").draw(win)

    a = 95.66
    e = 1
    for q in range(0,13):
        line = Line(Point(a,20), Point(a,40))
        line.draw(win)
        message = Text(Point(a,50), e ).draw(win)
        a = a + 95.66
        e = e + 1

    b = 23.9575
    for y in range(0,13):
        line = Line(Point(b, 35), Point(b, 40))
        line.draw(win)
        b = b + 95.66

    c = 47.915
    for ty in range(0,13):
        line = Line(Point(c, 30), Point(c, 40))
        line.draw(win)
        c = c + 95.66

    d = 71.8725
    for xy in range(0,13):
        line = Line(Point(d, 35), Point(d, 40))
        line.draw(win)
        d = d + 95.66

main()

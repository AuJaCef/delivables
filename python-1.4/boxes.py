#notes
#Austin C 11/20/18
#for notes

from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(50,50), Point(20, 20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        ob = shape.clone()
        ob.move(dx,dy)
        ob.draw(win)
    label = Text(Point(100,100), "Click again to quit")
    label.draw(win)
    win.getMouse()
    win.close()
main()

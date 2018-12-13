#Five click house
#Austin Cefaratti 12/10/18
#Allows user to draw a house in 5 mouse clicks

from graphics import *

def main():
    win = GraphWin("Our house", 300, 300)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    #message = Text(Point(5, 0.5), "Click on two points" )
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    rect = Rectangle(p1,p2)
    rect.draw(win)
    

    p3 = win.getMouse()
    p8=Point(p3.getX() + 1.1,p1.getY())
    door = Rectangle(p3,p8)
    door.draw(win)

    p4 = win.getMouse()
    p4.draw(win)
    p4a = Point(p4.getX() +0.55, abs(p4.getY() - 0.55))
    p4a.draw(win)
    window = Rectangle(p4, p4a)
    window.draw(win)
    
    p5 = win.getMouse()
    point = Point(p5.getX(),p5.getY())
    point.draw(win)
    dy = p2.getY() - p1.getY()
    p5a = Point(p1.getX(), p1.getY() + dy)
    p5a.draw(win)
    tri = Polygon(p5a, p5, p2)
    tri.draw(win)
main()

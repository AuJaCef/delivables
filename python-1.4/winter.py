#Winter
#Austin C 11/20/18
#Creates a winter scene

from graphics import *

def main():
    
    win = GraphWin("winter",500, 500)
    center = Point(100, 450)
    circ = Circle(center, 50)
    circ.setFill('white')
    circ.draw(win)

    center = Point(100, 405)
    circ = Circle(center, 45)
    circ.setFill('white')
    circ.draw(win)

    center = Point(100, 360)
    circ = Circle(center, 40)
    circ.setFill('white')
    circ.draw(win)

    rect = Rectangle(Point(73, 320), Point( 127, 250))
    rect.setFill('black')
    rect.draw(win)


    rect = Rectangle(Point(50, 320), Point( 150, 340))
    rect.setFill('black')
    rect.draw(win)

    rect = Rectangle(Point(73, 280), Point( 127, 300))
    rect.setFill('red')
    rect.draw(win)

    center = Point(80, 360)
    circ = Circle(center, 5)
    circ.setFill('black')
    circ.draw(win)

    center = Point(120, 360)
    circ = Circle(center, 5)
    circ.setFill('black')
    circ.draw(win)

    rect = Rectangle(Point(300, 500), Point( 350, 400))
    rect.setFill('brown')
    rect.draw(win)

    poly = Polygon(Point(240,450),Point(410,450),Point(325,350))
    poly.setFill('green')
    poly.draw(win)

    poly = Polygon(Point(240,390),Point(410,390),Point(325,290))
    poly.setFill('green')
    poly.draw(win)

    poly = Polygon(Point(240,340),Point(410,340),Point(325,240))
    poly.setFill('green')
    poly.draw(win)


    
main()

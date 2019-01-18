#animation
#Austin Cefaratti 1/18/19
#has a circle bounce around the screen

from graphics import*


def main():
    win = GraphWin("bouncing circle",200,200)
    center = Point(100, 100)
    circle = Circle(center, 10)
    circle.setFill('blue')
    circle.draw(win)
    xm = 1
    ym = 1
    for i in range(10000):
        circlec = circle.getCenter()
        xc = circlec.getX()
        yc = circlec.getY()
        
        if xc == 200 or xc == 0:
            xm = xm * -1
            
        if yc == 200 or yc == 0:
            ym = ym * -1
        circle.move(xm,ym)

        update(20)
        
main()

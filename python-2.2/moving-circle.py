#Moving circle
#Austin Cefaratti 1/16/19
#mover the circle to where the user clicks

from graphics import*

def moveTo(shape, newCenter):
    win = GraphWin("circle moving", 500,500)
    circle = Circle(Point(250,250), shape)
    circle.setFill("yellow")
    circle.draw(win)
    circle2 = Circle(Point(0,0), 0)
    circle2.draw(win)
    for i in range(10):
        newCenter = win.getMouse()
        circle2.undraw()
        newX = newCenter.getX()
        newY = newCenter.getY()
        circle2 = Circle(Point(newX,newY), shape)
        circle2.setFill("yellow")
        circle2.draw(win)
        circle.undraw()
    print("Click again to quit")
    win.getMouse()
    win.close()
def main():
    shape = eval(input("Enter the radius of the circle you want: "))
    print("Click in the box to move the circle.")
    newCenter = 0
    moveTo(shape, newCenter)
    




main()

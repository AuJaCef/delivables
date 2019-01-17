#Draw face new
#Austin Cefaratti 1/16/19
#Draws a face but again

from graphics import*

def drawFace(center, size, win):
    x1 = center.getX()
    y1 = center.getY()
    head = Circle(Point(x1, y1), size)
    head.setFill(color_rgb(255,187,133))
    head.draw(win)

    eye = Circle(Point(x1 - x1/size - 10, y1- y1/size - 10), size/10)
    eye.setFill("black")
    eye.draw(win)

    eye = Circle(Point(x1 - x1/size + 10, y1- y1/size - 10), size/10)
    eye.setFill("black")
    eye.draw(win)

    mouth = Circle(Point(x1, y1 + 20), size/5)
    mouth.setFill("black")
    mouth.draw(win)
    
def main():
    win = GraphWin("Faces",300,300)
    l = eval(input("How many faces do you want: "))
    for i in range(l):
        size = eval(input("How big do you want the face: "))
        print()
        print("Click where you want the face to be.")
        center = win.getMouse()
        drawFace(center, size, win)
main()

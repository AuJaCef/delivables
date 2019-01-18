#Archer plus
#Austin Cefaratti 1/18/19
#Allows the user to "shoot" arrows

from graphics import*
import math

def main():
    win = GraphWin()
    win.setCoords(-100,-100,100,100)
    center = Point(0, 0)
    circ = Circle(center, 50)
    circ.setFill('white')
    circ.draw(win)
    
    center = Point(0, 0)
    circ = Circle(center, 40)
    circ.setFill('black')
    circ.draw(win)
    
    center = Point(0, 0)
    circ = Circle(center, 30)
    circ.setFill('blue')
    circ.draw(win)
    
    center = Point(0, 0)
    circ = Circle(center, 20)
    circ.setFill('red')
    circ.draw(win)
    
    center = Point(0, 0)
    circ = Circle(center, 10)
    circ.setFill('yellow')
    circ.draw(win)
    numa = 5
    score = 0
    for i in range(5):
        print("You have",numa,"arrows remaining.")
        arrow = win.getMouse()
        circl = Circle(arrow, 2)
        circl.setFill('brown')
        circl.draw(win)
        ccenter = arrow
        xc = ccenter.getX()
        yc = ccenter.getY()
        d = math.sqrt(xc ** 2 + yc ** 2)
        print()
        print(d)
        print()
        if 50 >= d > 40:
            score = score + 1
        elif 40 >= d > 30:
            score = score + 3
        elif 30 >= d > 20:
            score = score + 5
        elif 20 >= d > 10:
            score = score + 7
        elif 10 >= d > 0:
            score = score + 9
        else:
            score = score + 0
        numa = numa - 1
    print("Your score is:",score)
        
main()

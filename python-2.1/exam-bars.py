#score exam
#Austin Cefaratti 1/4/18
#Gets the scores from a teacher withhorezontal bars

from graphics import*

import math

def main():
    win = GraphWin("Exam scores horizontal bars 1", 300, 300)
    Text(Point(100, 150), "Enter amount of students: ").draw(win)
    r = Entry(Point(240, 150), 10).draw(win)
    Text(Point(100, 250), "Click to continue after number is entered").draw(win)
    Text(Point(150, 60), "Note: If you enter a massive number,").draw(win)
    Text(Point(150, 80), "it could crash your computer").draw(win)
    win.getMouse()
    ra = r.getText()
    ra = eval(ra)
    win.close()
    x12 = 300
    x1 = 600
    y1 = 50 * ra
    x2 = 100
    y2 = 50
    y3 = 40
    y4 = 60
    x3 = 25
    x4 = 0
    y5 = 50
    b = 1
    c = 50
    a = 10
    win2 = GraphWin("Exam scores horizontal bars 2", x12, y1)
    win3 = GraphWin("Exam scores horizontal bars 3", x1, y1)
    Text(Point(150,20), "Click after entering number").draw(win2)
    for i in range(ra):
        Text(Point(x2,y2),"Enter student score (0 - 100): ").draw(win2)
        t = Entry(Point(250, y5), 10).draw(win2)
        win2.getMouse()
        ta = t.getText()
        ta = int(ta)
        Text(Point(a,c), b).draw(win3)
        y2 = y2 + 40
        y5 = y5 + 40
        b = b + 1
        c = c + 40
        x4 = 5 * ta
        rect = Rectangle(Point(x3, y3),Point(x4, y4))
        rect.setFill("blue")
        rect.draw(win3)
        y4 = y4 + 40
        y3 = y3 + 40
    Text(Point(150,10), "Click again to close this window").draw(win2)
    win2.getMouse()
    win2.close()
    win3.getMouse()
    win3.close()
            
        
            
        
        
    

main()

#Histogram
#Austin Cefaratti 1/4/18
#Graphs the amount of people that got a set score

from graphics import*

def main():
    win = GraphWin("Exam scores histogram bars 1", 300, 300)
    Text(Point(140, 10), "This program makes a histogram").draw(win)
    Text(Point(100, 150), "Enter amount of students: ").draw(win)
    r = Entry(Point(240, 150), 10).draw(win)
    Text(Point(150, 250), "Click to continue after number is entered").draw(win)
    win.getMouse()
    ra = r.getText()
    ra = eval(ra)
    win.close()
    x12 = 300
    x1 = 605
    y1 = 50 * ra
    x2 = 100
    y2 = 50
    y3 = 40
    y4 = 60
    x3 = 25
    x4 = 0
    y5 = 50
    y6 = 300
    b = 1
    c = 50
    a = 10
    u = 25
    q = 0
    p = 250
    az = 0
    pa = 0
    pb = 0
    pc = 0
    pd = 0
    pe = 0
    pf = 0
    pg = 0
    ph = 0
    pi = 0
    pj = 0
    win2 = GraphWin("Exam scores histogram  2", x12, y1)
    win3 = GraphWin("Exam scores histogram  bars 3", x1, y6)
    for i in range(ra):
        Text(Point(x2,y2),"Enter student score (0 - 10): ").draw(win2)
        t = Entry(Point(250, y5), 10).draw(win2)
        win2.getMouse()
        ta = t.getText()
        ta = int(ta)
        y2 = y2 + 40
        y5 = y5 + 40
        b = b + 1
        c = c + 40
        x4 = 5 * ta
        if ta == 0:
            pa = pa + 1
        elif ta == 1:
            pb = pb + 1
        elif ta == 2:
            pc = pc + 1
        elif ta == 3:
            pd = pd + 1
        elif ta == 4:
            pe = pe + 1
        elif ta == 5:
            pf = pf + 1
        elif ta == 6:
            pg = pg + 1
        elif ta == 7:
            ph = ph + 1
        elif ta == 8:
            pi = pi + 1
        elif ta == 9:
            pj = pj + 1
        else:
            az = az + 1      
    line = Line(Point(0,225), Point(600,225))
    line.draw(win3)
    for i in range(11):
        Text(Point(u, p), q ).draw(win3)
        q = q + 1
        u = u + 55
    
    sa = int(225 - (pa * 20))
    rect0 = Rectangle(Point(0, 225), Point(55, sa))
    rect0.setFill('red')
    rect0.draw(win3)

    sb = int(225 - (pb * 20))
    rect1 = Rectangle(Point(55, 225), Point(110, sb))
    rect1.setFill('orange')
    rect1.draw(win3)

    sc = int(225 - (pc * 20))
    rect2 = Rectangle(Point(110, 225), Point(165, sc))
    rect2.setFill('yellow')
    rect2.draw(win3)

    sd = int(225 - (pd * 20))
    rect3 = Rectangle(Point(165, 225), Point(220, sd))
    rect3.setFill('green')
    rect3.draw(win3)

    se = int(225 - (pe * 20))
    rect4 = Rectangle(Point(220, 225), Point(275, se))
    rect4.setFill('blue')
    rect4.draw(win3)

    sf = int(225 - (pf * 20))
    rect5 = Rectangle(Point(275, 225), Point(330, sf))
    rect5.setFill('purple')
    rect5.draw(win3)
    
    sg = int(225 - (pg * 20))
    rect6 = Rectangle(Point(330, 225), Point(385, sg))
    rect6.setFill('grey')
    rect6.draw(win3)

    sh = int(225 - (ph * 20))
    rect7 = Rectangle(Point(385, 225), Point(440, sh))
    rect7.setFill('aqua')
    rect7.draw(win3)

    sj = int(225 - (pi * 20))
    rect8 = Rectangle(Point(440, 225), Point(495, sj))
    rect8.setFill('pink')
    rect8.draw(win3)

    sk = int(225 - (pj * 20))
    rect9 = Rectangle(Point(495, 225), Point(550, sk))
    rect9.setFill('brown')
    rect9.draw(win3)

    sl = int(225 - (az * 20))
    rect10 = Rectangle(Point(550, 225), Point(605, sl))
    rect10.setFill('black')
    rect10.draw(win3)
main()

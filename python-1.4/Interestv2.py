#Updated intrest
#Austin C 11/20/18
#Does intrest along with giving a bar graph

from graphics import *

import math

def main():
    #intro
    print("Hello user, this program draws a graph based off your intrest.")

    #gets values for principal and intrest
    #principal = float(input("Enter your inital principal: "))
    #apr = float(input("What is the annualized intrest rate: "))
    
    
    win = GraphWin("Future value calculator", 300, 300)
    Text(Point(75, 150), " Enter principal: "). draw(win)
    Text(Point (75, 200), "Enter interest rate: ").draw(win)
    p = Entry(Point(200, 200), 10).draw(win)
    a = Entry(Point(200, 150), 10).draw(win)
    Text(Point(100, 10), "Click to exit").draw(win)
    win.getMouse()
    principal = p.getText()
    principal = eval(principal)
    apr = a.getText()
    apr = eval(apr)
    win.close()
    
    wina = GraphWin("Investment growth chart", 320, 240)
    inputText = Entry(Point(2.25, 3), 5)
    #Draw label " 0.0k" at (20, 230)
    Text(Point(20, 230), ' 0.0K').draw(wina)
    #Draw label " 2.5k" at (20, 180)
    Text(Point(20, 180), ' 2.5K').draw(wina)
    #Draw label " 5.0k" at (20, 130)
    Text(Point(20, 130), ' 5.0K').draw(wina)
    #Draw label " 7.5k" at (20, 80)
    Text(Point(20, 80), ' 7.5K').draw(wina)
    #Draw label "10.0k" at (20, 30)
    Text(Point(20, 30), '10.0K').draw(wina)
    #Draw a rectangle from (40,230) to (65, 230 - principal * 0.02)
    height = principal * 0.02
    bar = Rectangle (Point(40,230), Point(65, 230-height))
    bar.setFill("blue")
    bar.setWidth(2)
    bar.draw(wina)

    for year in range (1, 11):
        principal = principal * (1 + apr)
        x11 = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(x11, 230), Point(x11 + 25, 230 - height))
        bar.setFill("blue")
        bar.setWidth(2)
        bar.draw(wina)

    button = Text(Point(160, 120), "Click to Quit")
    button.draw(wina)
    Rectangle(Point(110, 100), Point(210, 140)).draw(wina)
    
    # wait for click and then quit
    wina.getMouse()
    wina.close()
    
main()

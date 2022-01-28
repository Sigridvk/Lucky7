
import turtle
import time

# in de display board:


colors = ['#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#000000', "#DDDDDD","#888888","yellow","blue","green","orange","magenta","purple","brown","darkgreen","gold","skyblue","darkred","turquoise","cyan","navy","lightgreen"]

def draw(board, myPen, window, sleep):
    window.tracer(False)
    myPen.color("#000000")
    fill_grid(30, len(board), board, myPen ,window)
    window.update()
    time.sleep(sleep)
    return window
    
# window.exitonclick()

def fill_grid(width, grid_length, board, myPen, window):
    topLeft_x=-150
    topLeft_y=150
    myPen.setheading(0)
    myPen.goto(topLeft_x,topLeft_y-width)
    myPen.pendown()
    for row in range (0,grid_length):
        for column in range (0,grid_length):
            if board[row][column]=='X':
                # square(width,grid[row][column])
                square(width, "red", myPen)
            elif board[row][column]!='':
                index = ord(board[row][column]) - 65
                square(width,colors[index], myPen)
            else:
                square(width, "white", myPen)
    		  
            myPen.penup()
            myPen.forward(width)
            myPen.pendown()
        myPen.setheading(270) 
        myPen.penup()
        myPen.forward(width)
        myPen.setheading(180) 
        myPen.forward(width*grid_length)
        myPen.setheading(0)
        myPen.pendown()
    myPen.penup()

def square(width,color, myPen):
    myPen.pendown()
    myPen.fillcolor(color)
    myPen.begin_fill()
    for i in range(0,4):
        myPen.forward(width)
        myPen.left(90)
    myPen.end_fill()
    myPen.setheading(0)
"""
draw.py

Programmeertheorie
Sigrid van Klaveren, Vanja Misuric-Ramljak and Luna Ellinger

- Contains the function to display a file with moves on a board.
- 
"""
import turtle
import csv
import time
import argparse
import sys
from sys import argv
import os.path

# Try to import the class Rushhour
try:
    sys.path.append("../")
    from Lucky7.code.classes.rushhour import Rushhour
except:
    print(f"Could not import the rushhour class. Please edit the path and try again")
    exit(9)

# These colors are used to display the vehicles 
colors = ['#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#000000', "#DDDDDD","#888888","yellow","blue","green","orange","magenta","purple","brown","darkgreen","gold","skyblue","darkred","turquoise","cyan","navy","lightgreen"]


def draw(board, myPen, window, sleep = 0):
    """
    Function that uses fill_grid to display the board with Turtle. 
    """
    window.tracer(False)
    myPen.color("#000000")
    fill_grid(30, len(board), board, myPen ,window)
    window.update()
    time.sleep(sleep)
    return window


def square(width,color, myPen):
    """
    Function that fills one square of the grid with a given color.
    """
    myPen.pendown()
    myPen.fillcolor(color)

    # Make a square with myPen and fill it with the color 
    myPen.begin_fill()
    for i in range(0,4):
        myPen.forward(width)
        myPen.left(90)
    myPen.end_fill()

    # Set heading of your pen east(0)
    myPen.setheading(0)

def fill_grid(width, grid_length, board, myPen, window):
    """
    
    """
    # Set pen to the left upper corner of the grid
    topLeft_x=-150
    topLeft_y=150
    myPen.setheading(0)
    myPen.goto(topLeft_x,topLeft_y-width)
    myPen.pendown()

    # Fill each square with function square 
    for row in range (0,grid_length):
        for column in range (0,grid_length):

            # check if the square contains the car X (red car)
            if board[row][column]=='X':
                square(width, "red", myPen)
            
            # Check if the square is not empty, if so fill square with color from list colors
            elif board[row][column]!='':
                index = ord(board[row][column]) - 65
                square(width,colors[index], myPen)

            # If the square contains no car, fill it with white
            else:
                square(width, "white", myPen)

            # Set your pen to the next square in column
            myPen.penup()
            myPen.forward(width)
            myPen.pendown()

        # Set your pen to the next row
        myPen.setheading(270) 
        myPen.penup()
        myPen.forward(width)
        myPen.setheading(180) 
        myPen.forward(width*grid_length)
        myPen.setheading(0)
        myPen.pendown()
    myPen.penup()



if __name__ == "__main__":

    # Create a command line argument parser
    parser = argparse.ArgumentParser(description='Display a rushhour game solution')
    parser.add_argument("-f", "--folder", help="folder in output folder", required=True)
    parser.add_argument("-i", "--input", help="input file (csv)", required=True)
    parser.add_argument("-g", "--game", help="gameboard", required=True)

    # Parse the command line arguments
    args = parser.parse_args()

    # Check command line arguments
    if len(argv) != 7:
        print(len(argv))
        print("Usage: python3 draw.py -f FILE -i INPUT -g GAMEBOARD")
        exit(1)

    folder = args.folder
    input_file = args.input
    file = f'output/{folder}/{input_file}.csv'

    # Create a rushhour object
    try:
        rushhourgame = Rushhour(args.game)
    except:
        print(f"An error occured: could not create rushhour game with the name: {args.game}. Please try again.")
        exit(2)

    # Open the given file
    try:
        csv_file = open(file)
    except:
        print(f"Could not open the file: {file}. Please check if you entered the right folder and filename")
        exit(3)

    # Read the csv file and skip the header
    with csv_file:
        try:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            next(csv_reader)
        except:
            print(f"Could not read csv file. An empty file is not accepted. Please try again")
            exit(4)
        
        # Iterate over each row and save the car, move
        for row in csv_reader:
            try:
                car = row[0]
                move = int(row[1])
            except:
                print("Could not display this board. Check if the file contains a car, step per row")
                exit(5)

            # Call the move method from the rushhour object and perform move
            try:
                rushhourgame.move(car, move)
            except:
                print(f"could not perform move: {move} on car: {car}")
                exit(6)

            # Create the board after the move was made
            try:
                board = rushhourgame.create_board()
            except:
                print(f"Error. Could not create board from rushhourgame object. Did you enter the right game on the commandline?")
                exit(7)
            
            # Call the draw function and display the move in turtle
            try:
                window = turtle.Screen()
                myPen = turtle.Turtle()
                draw(board, myPen, window, 0.2)
            except:
                print(f"Error. Could not display the board.")
                exit(8)

        # When all moves are done, exit the turtle window by clicking on it
        window.exitonclick()
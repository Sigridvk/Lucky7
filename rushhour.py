"""
 rushhour.py

 Programmeertheorie
 Sigrid van Klaveren, Vanja Misuric-Ramljak and Luna Ellinger
"""

import argparse
import csv
import math
import algo1
import turtle
import time


# dit heb ik vrijwel allemaal
window = turtle.Screen()
myPen = turtle.Turtle()
window.tracer(False)
myPen.color("#000000")
topLeft_x=-150
topLeft_y=150
colors = ['#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']


    # print(random_element[0][0])
def fill_grid(width, grid_length, board):
    """
    Calls the function square to draw all the seperate squares of the grid
    """
    myPen.penup()
    myPen.setheading(0)
    myPen.goto(topLeft_x,topLeft_y-width)
    myPen.pendown()
    for row in range (0,grid_length):
        for column in range (0,grid_length):
            
            # If the carletter is X, the car is red
            if board[row][column]=='X':
                square(width, "red")

            # If there is a different car, it chooses a color from the list colors 
            elif board[row][column]!='':
                index = ord(board[row][column]) - 65
                square(width,colors[index])

            # If there is no car, it draws a white square
            else:
                square(width, "white")
    		  
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


def square(width,color):
    """
    Draws one square in the grid with the given color
    """
    myPen.pendown()
    myPen.fillcolor(color)
    myPen.begin_fill()
    for i in range(0,4):
        myPen.forward(width)
        myPen.left(90)
    myPen.end_fill()
    myPen.setheading(0)

class rushhour():

    def __init__(self, output_file, game):
        """
        Initializes the RushHour game by creating an empty list for the moves of the vehicles and writing the information of
        the begin-state of the gameboard to a nested dictionary.
        Takes the output filename and filename of the game as parameter that was specified at the command line.
        Returns nothing.
        """

        # List for moves of the vehicles
        self.moves = []

        # Define game file
        file = f'gameboards/{game}.csv'

        # Size grid is defined by 8th character of the gamename, example: Rushhour6x6_1
        self.size_board = int(game[8])

        reader = csv.reader(open(file))
        
        # Load information into a nested dictionary
        self.dict = {}
        for row in list(reader)[1:]:
            key = row[0]
            self.dict[key] = {"orientation": row[1], "col": int(row[2]), "row": int(row[3]),"length": int(row[4])}


    def create_board(self):
            """
            Creates the gameboard by extracting data from the nested dictionary with information about the state of the board.
            Takes no parameters other than self.
            Returns the gameboard.
            """

            # Create empty list for grid
            self._board = []

            # Fill empty grid with lists and list elements
            for board_row in range(self.size_board):
                self._board.append([])
                for column in range(self.size_board):
                    self._board[board_row].append('')

            # For loop over rows in df
            for vehicle in self.dict:

                # Define vehicle properties
                name = vehicle
                orientation = self.dict[vehicle]["orientation"]
                col = self.dict[vehicle]["col"] - 1
                row = self.dict[vehicle]["row"] - 1
                length = self.dict[vehicle]["length"]

                # Horizontal orientation
                if orientation == "H":

                    # Add vehicle to board
                    for i in range(length):
                        self._board[row][col + i] = name

                # Vertical orientation
                else:

                    # Add vehicle to board
                    for i in range(length):
                        self._board[row +  i ][col] = name
        
            return self._board

    
    def move(self, car, steps):
        """
        'Moves' the vehicle by the defined amount of steps to a new spot on the board.
        Takes the vehicle and the number of steps the car has to take as parameters.
        Returns nothing.
        """
        
        # Define move and append to moves
        move = (car, steps)
        self.moves.append(move)

        # Horizontal
        if self.dict[car]['orientation'] == 'H':
            
            # Redefine column coordinate vehicle
            self.dict[car]['col'] += steps

        # Vertical
        else:
            # Redefine row coordinate vehicle
            self.dict[car]['row'] -= steps
    

    def display_board(self, board):
        """
        Prints the board to the terminal.
        Takes the board as parameter.
        Returns nothing.
        """
        # for row in board:
        #     print(row)
        # print()

        # show the board in turtle, 30 = width squares, 6 = length board
        fill_grid(30, 6, board)
        window.update()

        # time the screen delays in seconds
        # time.sleep(0.5)

    def solved(self, board):
        """
        Checks whether the current board is the solution.
        If the space next to the exit == 'X' the problem is solved.
        """

        # Calculate the coordinates of the square before the exit as index
        exit_row = math.floor((self.size_board+1)/2) - 1
        exit_col = self.size_board-1

        if board[exit_row][exit_col] == 'X':
            print("You solved the puzzle! 1")
            return True


if __name__ == "__main__":

    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description="")

    # Adding arguments
    parser.add_argument("output", help="output file (csv)")
    parser.add_argument("-g", "--game", type=str)

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provided arguments
    rushhourgame = rushhour(args.output, args.game)

    # # Initialize begin state board
    # board = rushhourgame.create_board()
    # i = 1
    # Infinite loop to play game, breaks when solution is found
    while True:

        # Initialize begin state board
        board = rushhourgame.create_board()

        # Display current state board (in terminal)
        rushhourgame.display_board(board)

        if rushhourgame.solved(board):
            break
        
        move_game = algo1.random_algorithm(rushhourgame.dict, board)
        step = move_game[1]
        car = move_game[0]
        
        print(f"move_game {move_game}")
        # print(step, car)
        if step == 0:
            pass
        else:
            rushhourgame.move(car, step)

    # Write moves to an output file
    with open('output/output_moves.csv','w') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['car','move'])
        for row in rushhourgame.moves:
            csv_out.writerow(row)


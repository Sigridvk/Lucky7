"""
 rushhour.py

 Programmeertheorie
 Sigrid van Klaveren, Vanja Misuric-Ramljak and Luna Ellinger

 - Contains the class rushhour.
"""
 
import os
import copy
import csv
import math
from ..visualisation.draw import draw
# import turtle

# Global variable for the total steps per solved game
solved_games = []

# Global variable for the game with smallest amount of steps
smallest_amount_steps = None

steps_from_smallest_game = []

# Variables to display the board in turtle
# Source: https://www.101computing.net/rush-hour-backtracking-algorithm/
# window = turtle.Screen()
# myPen = turtle.Turtle()


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

        self._board = []
        # self.steps_from_smallest_game = []

        # Define game file
        file = f'gameboards/{game}.csv'

        index_x = game.find('x')

        # Size grid is defined by 8th character of the gamename, example: Rushhour6x6_1
        self.size_board = int(game[8:index_x])

        reader = csv.reader(open(file))
        
        # Load information into a nested dictionary
        self.dict = {}
        for row in list(reader)[1:]:
            key = row[0]
            # self.dict[key] = {"orientation": row[1], "col": int(row[2]), "row": int(row[3]),"length": int(row[4])}
            self.dict[key] = {"orientation": row[1], "col": (int(row[2]) - 1), "row": (int(row[3]) - 1),"length": int(row[4])}
        
        self._greedy_cars = list(self.dict.keys())
        # self._greedy_cars.remove("X")

        self._greedy_cars_all = list(self.dict.keys())
        # self._greedy_cars_all.remove("X")

        # print(self._greedy_cars)


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
                # col = self.dict[vehicle]["col"] - 1
                col = self.dict[vehicle]["col"]
                # row = self.dict[vehicle]["row"] - 1
                row = self.dict[vehicle]["row"]
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

        # print(f"car: {car}")
        # print(f"car: {steps}")
        
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
        
        self.create_board()
        self.display_board()
    

    def display_board(self):
        """
        Prints the board to the terminal.
        Takes the board as parameter.
        Returns nothing.
        """
        # board = self._board
        # window = turtle.Screen()
        # myPen = turtle.Turtle()
        # # # show the board in the terminal with lists in a list
        # # for row in board:
        # #     print(row)
        # # print()

        # # show the board in turtle, 30 = width squares, 6 = length board
        # draw(board, myPen, window, 0)
        # window.update()


    def solved(self):
        """
        Checks whether the current board is the solution.
        If the space next to the exit == 'X' the problem is solved.
        """
        board = self._board
        # Calculate the coordinates of the square before the exit as index
        exit_row = math.floor((self.size_board+1)/2) - 1
        exit_col = self.size_board-1


        if board[exit_row][exit_col] == 'X':
            # self.display_board(board)
            # print("You solved the puzzle! 1")
            return True

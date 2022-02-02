"""
 rushhour.py

 Programmeertheorie
 Sigrid van Klaveren, Vanja Misuric-Ramljak and Luna Ellinger

 - Contains the class Rushhour which holds methods that represent a RushHour game.
"""
 
import os
import csv
import math
import sys
import turtle


class Rushhour():

    def __init__(self, game):
        """
        Initializes the RushHour game by creating an empty list for the moves of the vehicles and writing the information of
        the begin-state of the gameboard to a nested dictionary.
        Takes the output filename and filename of the game as parameter that was specified at the command line.
        """

        # List for moves of the vehicles
        self.moves = []
        self._board = []

        # Define game file
        file = f'gameboards/{game}.csv'

        # Size grid is defined by 8th character of the gamename, example: Rushhour6x6_1
        index_x = game.find('x')
        self.size_board = int(game[8:index_x])

        reader = csv.reader(open(file))
        
        # Load information into a nested dictionary
        self.dict = {}
        for row in list(reader)[1:]:
            key = row[0]
            self.dict[key] = {"orientation": row[1], "col": (int(row[2]) - 1), "row": (int(row[3]) - 1),"length": int(row[4])}
        
        # Define lists that will be used by the greedy algorithms
        # A list from which cars will be removes which surely can't move
        self._greedy_cars = list(self.dict.keys())

        # A list which will always contain all cars
        self._greedy_cars_all = list(self.dict.keys())
        self._path = ""


    def create_board(self):
            """
            Creates the gameboard by extracting data from the nested dictionary with information about the state of the board.
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
                col = self.dict[vehicle]["col"]
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
            self.dict[car]['row'] -= step


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
            return True

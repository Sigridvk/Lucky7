"""
 rushhour.py

 Programmeertheorie
 Sigrid van Klaveren, Vanja Misuric-Ramljak and Luna Ellinger

 Usage: python3 rushhour.py -g GAME -o OUTPUT [-n NUMER_OF_RUNS]
"""

import argparse
import os
import csv
import math
import algorithms.algo1 as algo1
import time
import datetime
from sys import argv
import draw
import matplotlib.pyplot as plt



# Global variable for the total steps per solved game
solved_games = []

# Global variable for the game with smallest amount of steps
smallest_amount_steps = None

moves_smallest_game = []

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
        # self.moves_smallest_game = []

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
        # window = turtle.Screen()
        # myPen = turtle.Turtle()
        # show the board in the terminal with lists in a list
        # for row in board:
        #     print(row)
        # print()

        # show the board in turtle, 30 = width squares, 6 = length board
        # draw.draw(board, myPen, window, 1)
        # window.update()


    def solved(self, board):
        """
        Checks whether the current board is the solution.
        If the space next to the exit == 'X' the problem is solved.
        """

        # Calculate the coordinates of the square before the exit as index
        exit_row = math.floor((self.size_board+1)/2) - 1
        exit_col = self.size_board-1

        if board[exit_row][exit_col] == 'X':
            # self.display_board(board)
            # print("You solved the puzzle! 1")
            return True


if __name__ == "__main__":

    start_time = time.time()
    print(datetime.datetime.now())

    # Create a command line argument parser
    parser = argparse.ArgumentParser(description='Solve a rushhour game')
    parser.add_argument("-g", "--game", type=str, help="gamefile name", required=True)
    parser.add_argument("-o", "--output", help="output file (csv)", required=True)
    parser.add_argument("-n","--runs", type=int, default=1, help="number of runs")

    # Parse the command line arguments
    args = parser.parse_args()

    # Check command line arguments
    if len(argv) not in [5,7]:
        print(len(argv))
        print("Usage: python3 rushhour.py -g GAME -o OUTPUT [-n NUMER_OF_RUNS]")
        exit(1)

    # Loop through algorithm n times
    for i in range(args.runs):
        # if (i%500 == 0):
        #     print (i)

        counter = 0

        # Run main with provided arguments
        rushhourgame = rushhour(args.output, args.game)

        # Initialize begin state board
        board = rushhourgame.create_board()

        # Display current state board (in terminal)
        # rushhourgame.display_board(board)

        # Infinite loop to play game, breaks when solution is found
        while True:

            # Initialize begin state board
            board = rushhourgame.create_board()

            # Display current state board (in terminal)
            # rushhourgame.display_board(board)

            # Check if the current game is solved, if so, break. Append total steps to list
            # MISSCHIEN DEZE FUNCTIE VERPLAATSEN, WORDT NU OOK GECHECKT NA EEN STAP VAN 0
            if rushhourgame.solved(board):
                solved_games.append(counter)
                break
            
            # Call first algorithm to decide which car to move
            move_game = algo1.random_algorithm(rushhourgame.dict, board)
            step = move_game[1]
            car = move_game[0]

            # If the step-size is 0, begin again, else move that car
            if step == 0:
                pass
            else:
                rushhourgame.move(car, step)
                counter += 1

        # Check whether the current game is run in the least amount of steps
        if smallest_amount_steps == None or smallest_amount_steps > counter:
            
            # Redefine smallest_amount_steps
            smallest_amount_steps = counter
            
            # Save steps to moves_smallest_game 
            moves_smallest_game = rushhourgame.moves

    # print("--- %s seconds ---" % (time.time() - start_time))

    # Write moves to an output file
    with open('output/algo_1/output_moves.csv','w') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['car','move'])
        for row in moves_smallest_game:
            csv_out.writerow(row)
    
    # Write total steps to an output file
    with open(f'output/algo_1/{args.output}','w') as out2:
        write = csv.writer(out2)
        for val in solved_games:
            write.writerow([val])
    

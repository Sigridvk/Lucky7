"""
 rushhour.py

 Programmeertheorie
 Sigrid van Klaveren, Vanja Misuric-Ramljak and Luna Ellinger
"""

import argparse
import csv


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


    # def check_move(self, car):
    #     """
    #     """

    #     # Check orientation
    #     if self.dict[car]['orientation'] == 'H':
            
    #         # Define coordinates spot on the right side of the vehicle
    #         row_right = self.dict[car]['row']
    #         column_right = self.dict[car]['col'] + self.dict[car]['length']

    #         # Check whether spot right from vehicle is empty
    #         if self._board[row_right][column_right] == '':

    #             # 'Move' car to the right, by emptying spot 
    #             self._board[self.dict[car]['row']][self.dict[car]['col']] = ''

    #             # Redefine coordinates vehicle
    #             self.dict[car]['row'] = row_right
    #             self.dict[car]['col'] += 1
        
    
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
        for row in board:
            print(row)
        print()       


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

    # Initialize begin state board
    board = rushhourgame.create_board()
    
    # Infinite loop to play game, breaks when solution is found
    while True:

        # Display current state board (in terminal)
        rushhourgame.display_board(board)
        break

    # A couple of hardcoded moves and boardprints to check the program (officially not part of the code)
    # Move 1
    rushhourgame.move('A', -1)

    # Create and print board
    board = rushhourgame.create_board()
    rushhourgame.display_board(board)

    # Move 2
    rushhourgame.move('C', -1)

    # Create and print board
    board = rushhourgame.create_board()
    rushhourgame.display_board(board)

    # Move 3
    rushhourgame.move('G', 2)       

    # Create and print board
    board = rushhourgame.create_board()
    rushhourgame.display_board(board)

    # Write moves to an output file
    with open('output/output_moves.csv','w') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['car','move'])
        for row in rushhourgame.moves:
            csv_out.writerow(row)


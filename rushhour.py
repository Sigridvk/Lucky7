"""
 rushhour.py

 Programmeertheorie
 Sigrid van Klaveren, Vanja Misuric-Ramljak and Luna Ellinger

 - ....
"""

import argparse
import pandas as pd


class rushhour():

    def __init__(self, output_file, game):
        """
        Initializes the RushHour game by creating an empty gameboard and writing the information of the
        begin-state of the gameboard to a Pandas Dataframe.
        Takes the output filename, filename of the game as parameter that was specified at the command line.
        Returns nothing.
        """

        # Create empty list for grid
        self._board = []

        # Define game file
        file = f'gameboards/{game}.csv'

        # Size grid is defined by 8th character of the gamename, example: Rushhour6x6_1
        size_grid = int(game[8])

        # Fill empty grid with lists and list elements
        for grid_row in range(size_grid):
            self._board.append([])
            for column in range(size_grid):
                self._board[grid_row].append('')
        

        # Write csv file to a Pandas dataframe
        self._board_state_info = pd.read_csv(file)


    def create_board(self):
        """
        Creates the gameboard by using the Pandas dataframe with info of the state of the board.
        Takes no parameters other than self.
        Returns the gameboard.
        """

        # For loop over rows in df
        for vehicle in range(len(self._board_state_info)):

            # Define vehicle properties
            name = self._board_state_info.loc[vehicle, "car"]
            orientation = self._board_state_info.loc[vehicle, "orientation"]
            col = int(self._board_state_info.loc[vehicle, "col"]) - 1
            row = int(self._board_state_info.loc[vehicle, "row"]) - 1
            length = int(self._board_state_info.loc[vehicle, "length"])

            # Horizontal orientation
            if orientation == "H":

                # Car
                if length == 2:
                    self._board[row][col] = name
                    self._board[row][col + 1] = name

                # Truck
                else:
                    self._board[row][col] = name
                    self._board[row][col + 1] = name
                    self._board[row][col + 2] = name

            # Vertical orientation
            else:

                # Car
                if length == 2:
                    self._board[row][col] = name
                    self._board[row + 1][col] = name

                # Truck
                else:
                    self._board[row][col] = name
                    self._board[row + 1][col] = name
                    self._board[row + 2][col] = name
       
        return self._board


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
    
    # Test
    for row in board:
        print(row)


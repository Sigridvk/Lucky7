"""
algo1.py

Programmeertheorie
Sigrid van Klaveren, Vanja Misuric-Ramljak and Luna Ellinger

- Contains the functions from the random algorithm that plays the game RushHour in a random manner.
"""

import random
from ..classes.rushhour import rushhour

# Global variable for the total steps per solved game
# solved_games = []
# smallest_amount_steps = None
# steps_from_smallest_game = []

def random_car(cars_dict):
    """
    Returns a random car from a dictionary of cars
    """
    return random.sample(cars_dict.items(), 1)


def random_move(moves_list):
    """
    Returns a random move from a list of possible moves
    """
    return random.choice(moves_list)


def check_move(car, cars_dict, board):
    """
    Returns a list of possible moves for a given car
    """
    # print(f"checked_car = {car}")

    # List of all possible moves
    moves_list = []

    # Check orientation
    if cars_dict[car]['orientation'] == 'H':
        
        # Define coordinates spot on the right side of the vehicle 
        # row = cars_dict[car]['row'] - 1
        row = cars_dict[car]['row']
        # column_right = cars_dict[car]['col'] + cars_dict[car]['length'] - 1
        column_right = cars_dict[car]['col'] + cars_dict[car]['length']

        # part of the list on the rightside of the car
        check_list = board[row][column_right:]

        # Loop through all spots to check if they are empty
        for i in range(len(check_list)):

            # Check whether spot right from vehicle is empty
            if board[row][column_right + i] == '':
                moves_list.append(i + 1)
            else:
                break

        # Define coordinates spot on the left side of the vehicle
        # column_left = cars_dict[car]['col'] - 1
        column_left = cars_dict[car]['col']

        # List of all spots to the left of the car
        check_list = board[row][:column_left]

        # Loop through all spots to check if they are empty
        for i in range(len(check_list) - 1, -1, -1):

            # Check whether spot left from vehicle is empty 
            if board[row][i] == '':
                moves_list.append(i -  column_left)
            else:
                break


    # Check orientation
    if cars_dict[car]['orientation'] == 'V':

        # Define coordinates spot on the above side of the vehicle
        # row_up = cars_dict[car]['row'] - 2
        row_up = cars_dict[car]['row'] - 1
        # column = cars_dict[car]['col'] - 1
        column = cars_dict[car]['col']

        # Check if there is a spot above the car
        if (row_up >=  0):

            # Check all spots above the car
            for i in range(row_up, -1, -1):

                # Check whether spot above the vehicle is empty
                if board[i][column] == '':

                    # If spot is empty, append to the possible moves
                    moves_list.append(row_up - i + 1)

                else:
                    break

        # Define coordinates spot on the down side of the vehicle
        # row_down = cars_dict[car]['row'] + cars_dict[car]['length'] - 1
        row_down = cars_dict[car]['row'] + cars_dict[car]['length']

        # Check if there are any spots below the car
        if (row_down < len(board)):
            
            # Loop through all spots below the car
            for i in range(row_down, len(board), 1):

                # Check whether spot down from vehicle is empty
                if board[i][column] == '':

                    # If the spot is empty, appen possible move to list
                    moves_list.append( -1 * (i - row_down + 1))

                else:
                    break
    # print(f"Car: {car} Moves list: {moves_list}")
    return moves_list


def random_algorithm(dict, board):
    """
    Random algorithm that picks a random car from the given dictionary.
    The algorithm checks which moves this car can make.
    Randomly select a move from the possible moves.
    Returns a list [car, step], step = 0 if the car can't move. """

    car = random_car(dict)[0][0]
    moves = check_move(car, dict, board)

    if moves:
        step = random_move(moves)
    else:
        step = 0 

    return [car, step]


def run_algorithm(rushhourgame, runs, smallest_amount_steps, steps_from_smallest_game, solved_games):
# def run_algorithm(runs, game):
    """
    """

    # Loop through algorithm n times
    for i in range(runs):

        counter = 0

        # Create rushhour game
        # rushhourgame = rushhour(output_file, game)

        # Infinite loop to play game, breaks when solution is found
        while True:

            # Initialize begin state board
            board = rushhourgame.create_board()

            # Check if the current game is solved, if so, break. Append total steps to list
            if rushhourgame.solved():
                solved_games.append(counter)
                break
            
            # Call first algorithm to decide which car to move
            move_game = random_algorithm(rushhourgame.dict, board)
            step = move_game[1]
            car = move_game[0]

            # If the step-size is 0, begin again, else move that car
            if step == 0:
                pass
            else:
                rushhourgame.move(car, step)
                counter += 1
            
            # rushhourgame.display_board()

        # Check whether the current game is run in the least amount of steps
        if smallest_amount_steps == None or smallest_amount_steps > counter:
            
            # Redefine smallest_amount_steps and save the steps from this game
            smallest_amount_steps = counter
            steps_from_smallest_game = rushhourgame.moves

    return [steps_from_smallest_game, solved_games]
    
    
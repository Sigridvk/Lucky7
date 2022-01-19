import random 

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

    # List of all possible moves
    moves_list = []

    # Check orientation
    if cars_dict[car]['orientation'] == 'H':
        
        # Define coordinates spot on the right side of the vehicle
        row = cars_dict[car]['row'] - 1
        column_right = cars_dict[car]['col'] + cars_dict[car]['length'] - 1

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
        column_left = cars_dict[car]['col'] - 1

        # List of all spots to the left of the car
        check_list = board[row][:column_left]

        for i in range(len(check_list) - 1, -1, -1):

            # Check whether spot left from vehicle is empty 
            if board[row][i] == '':

                moves_list.append(i -  column_left)

            else:
                break


    # Check orientation
    if cars_dict[car]['orientation'] == 'V':

        # Define coordinates spot on the above side of the vehicle
        row_up = cars_dict[car]['row'] - 2
        column = cars_dict[car]['col'] - 1

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
        row_down = cars_dict[car]['row'] + cars_dict[car]['length'] - 1

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

        
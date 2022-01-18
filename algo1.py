import random 

def random_car(cars_dict):
    return random.sample(cars_dict.items(), 1)

def random_move(moves_list):
    return random.choice(moves_list)


def check_move(car, cars_dict, board):
    """
    """

    moves_list = []

    # Check orientation
    if cars_dict[car]['orientation'] == 'H':
        
        # Define coordinates spot on the right side of the vehicle
        row = cars_dict[car]['row'] - 1
        column_right = cars_dict[car]['col'] + cars_dict[car]['length'] - 1

        check_list = board[row][column_right:]

        for i in range(len(check_list)):

            # Check whether spot right from vehicle is empty
            if board[row][column_right + i] == '':

                # moves_list.append(board[row_right][column_right + i])

                moves_list.append(i + 1)

            else:
                break

        # Define coordinates spot on the left side of the vehicle
        column_left = cars_dict[car]['col'] - 1

        check_list = board[row][:column_left]

        for i in range(len(check_list) - 1, -1, -1):

            # Check whether spot left from vehicle is empty
            if board[row][i] == '':

                # moves_list.append(board[row_right][column_right + i])

                moves_list.append(i -  column_left)

            else:
                break


    #  # Check orientation
    # if cars_dict[car]['orientation'] == 'V':
        
    #     # Define coordinates spot on the above side of the vehicle
    #     row_up = cars_dict[car]['row'] - 1
    #     column = cars_dict[car]['col'] - 1

    #     check_list = board[row_up:][column]

    #     for i in range(len(check_list) - 1, -1, -1):

    #         # Check whether spot right from vehicle is empty
    #         if board[i][column] == '':

    #             # moves_list.append(board[row_right][column_right + i])

    #             moves_list.append(i - row_up)

    #         else:
    #             break

    #     # Define coordinates spot on the down side of the vehicle
    #     row_down = cars_dict[car]['row'] + cars_dict[car]['length'] - 1

    #     check_list = board[:row_down][column]

    #     for i in range(len(check_list)):

    #         # Check whether spot down from vehicle is empty
    #         if board[row_down + i][column] == '':

    #             # moves_list.append(board[row_right][column_right + i])

    #             moves_list.append(i + 1)

    #         else:
    #             break

    print(moves_list)
    print(car)
    return moves_list

def random_algorithm(dict, board):

    car = random_car(dict)[0][0]
    moves = check_move(car, dict, board)

    if moves:
        step = random_move(moves)
    else:
        step = 0 

    return [car, step]

        
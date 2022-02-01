"""
breadth.py

Programmeertheorie
Sigrid van Klaveren, Vanja Misuric-Ramljak and Luna Ellinger

- Contains the class Greedy which holds methods to run the greedy1 and greedy2 algorithm.
- Algorithms play the game RushHour use random functions and heuristics. 
- Both algorithms will not undo moves by moving the same car back and forth.
- Greedy1 will also try to move the red car forward when possible, Greedt2 won't.
"""

from . import randomise
import random
import copy

class Greedy():

    def __init__(self, game):
        self._game = game

        # Defines the vehicle blocking the red car
        self._blocking_vehicle = ""

        # Will contain the steps made
        self._moves = []

        # Will be updated when a move is made 
        self._count_moves = 0

        # Will contain the last move
        self._last_move = []


    def red_car_forward(self):
        """
        Moves the red car forward if possible.
        """
        
        # Define coordinate right to red car
        column_ = self._game.dict['X']['col'] + 2
        row =  self._game.dict['X']['row']
        
	    # Check if red car can move
        for i in range(column_, self._game.size_board):
            if self._game._board[row][i] == '':
                
                # move the red car
                self._game.move('X', 1)
                self._count_moves += 1

            # Redefine the blocking car and break loop
            else:
                self._blocking_vehicle = self._game._board[row][i]
                break


    def greedy_random_car(self):
        """
        Returns a random car from a dictionary of cars.
        """

        return random.choice(self._game._greedy_cars)


    def greedy_random_algorithm(self):
        """
        Random algorithm that picks a random car from the given dictionary.
        The algorithm checks which moves this car can make, randomly selects a move from the possible moves.
        Returns a list [car, step], step = 0 if the car can't move. 
        """
        
        # Pick a car from the board and create the possible moves
        car = self.greedy_random_car()
        moves = randomise.check_move(car, self._game.dict, self._game._board)

        if moves:

            # Pick one step from the 
            move = randomise.random_move(moves)

            # Append all cars to the list after a move has been made
            all_cars = self._game._greedy_cars_all
            all_cars = copy.deepcopy(all_cars)
            self._game._greedy_cars = all_cars

        else:
            move = 0

            # Remove car from list when car could not move
            self._game._greedy_cars.remove(car)
        return [car, move]


    def run_random_greedy1(self):
        """
        Runs the greedy algorithm WITHOUT moving the red car forward when possible.
        """

        self._game.create_board()
        vehicle = ""

        # While loop will break when game is solved
        while not self._game.solved():

            self._game.create_board()
            if self._game.solved():
                break
                
            # Pick a vehicle and a move
            move_game = self.greedy_random_algorithm()
            move = move_game[1]
            vehicle = move_game[0]

            # If the step-size is 0, begin again, else move that car
            if move == 0:
                pass

            # Don't make the move if it has just been made
            elif move_game == self._last_move:
                pass

            # Move the vehicle
            else:
                self._game.move(vehicle, move)

                # Save last step so that no move back will be made
                self._last_move = [vehicle, (move*-1)]

                # Count the steps
                self._count_moves += 1

                # Save move
                self._moves.append((vehicle, move))
    

    def run_random_greedy2(self):
        """
        Runs the greedy algorithm BY moving the red car forward when possible.
        """
        
        self._game.create_board()
        vehicle = ""

        # While loop will break when game is solved
        while not self._game.solved():

            self._game.create_board()

            # If the current vehicle was blocking the red car, try to move the red car forward
            if vehicle == self._blocking_vehicle:
                self.red_car_forward()

            if self._game.solved():
                break
            
            # Pick a vehicle and a move
            move_game = self.greedy_random_algorithm()
            move = move_game[1]
            vehicle = move_game[0]

            # If the step-size is 0, begin again, else move that car
            if move == 0:
                pass

            # Don't make the move if it has just been made
            elif move_game == self._last_move:
                pass

            # Move the vehicle
            else:
                self._game.move(vehicle, move)

                # Save last step so that no move back will be made
                self._last_move = [vehicle, (move*-1)]

                # Count the steps
                self._count_moves += 1

                # Save move
                self._moves.append((vehicle, move))




            


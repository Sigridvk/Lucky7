# from ..classes.rushhour import rushhour

from . import algo1
import random
import copy

class Greedy():
    """
    """

    def __init__(self, game):
        self._game = game
        self.blocking_car = ""
        self._steps = []
        self._count_steps = 0
        self._last_step = []


    def red_car_forward(self):
        
        # Define coordinate right to red car
        column_ = self._game.dict['X']['col'] + 2
        row =  self._game.dict['X']['row']
        
	    # Check if red car can move
        for i in range(column_, self._game.size_board):
            if self._game._board[row][i] == '':
                
                # move the red car
                self._game.move('X', 1)
                self._count_steps += 1

            else:
                self.blocking_car = self._game._board[row][i]
                break

    def greedy_random_car(self):
        """
        Returns a random car from a dictionary of cars
        """
        return random.choice(self._game._greedy_cars)


    # def greedy_random_move(self):
    # """
    # Returns a random move from a list of possible moves
    # """
    # return random.choice(moves_list)


    def greedy_random_algorithm(self):
        """
        Random algorithm that picks a random car from the given dictionary.
        The algorithm checks which moves this car can make.
        Randomly select a move from the possible moves.
        Returns a list [car, step], step = 0 if the car can't move. 
        """
        
        car = self.greedy_random_car()
        moves = algo1.check_move(car, self._game.dict, self._game._board)

        if moves:
            step = algo1.random_move(moves)

            # Append all cars to the list after a move has been made
            all_cars = self._game._greedy_cars_all
            all_cars = copy.deepcopy(all_cars)

            self._game._greedy_cars = all_cars
            # print(f"all cars {all_cars}")

        else:
            step = 0

            # Remove car from list when car could not move
            self._game._greedy_cars.remove(car)
            # print(f"not all cars {self._game._greedy_cars}")
            
        return [car, step]


    def run_random_greedy(self):
        self._game.create_board()
        car = ""
        # self._count_steps = 0
        while not self._game.solved():
        
        # for i in range(1):
            # if car == self.blocking_car:
            #     self.red_car_forward()

            if self._game.solved():
                break

            # while car != self.blocking_car:
            # move_game = algo1.random_algorithm(self._game.dict, self._game._board)

            move_game = self.greedy_random_algorithm()
            step = move_game[1]
            car = move_game[0]

            # If the step-size is 0, begin again, else move that car
            if step == 0:
                pass
            elif move_game == self._last_step:
                pass
            else:
                self._game.move(car, step)

                # Save last step so that no move back will be made
                self._last_step = [car, (step*-1)]

                self._count_steps += 1
                self._steps.append((car, step))
            


            # self._game.dict['X']['column'] = column_
    




            


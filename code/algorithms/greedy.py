# from ..classes.rushhour import rushhour

from . import algo1

class Greedy():
    """
    """

    def __init__(self, game):
        self._game = game
        self.blocking_car = ""
        self._steps = []
        self._count_steps = 0


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


    def run_random_greedy(self):
<<<<<<< HEAD
        
=======
        self._game.create_board()
        car = ""
        # self._count_steps = 0
        while not self._game.solved():
        # for i in range(1):
            if car == self.blocking_car:
                self.red_car_forward()

            if self._game.solved():
                break

            # while car != self.blocking_car:
            move_game = algo1.random_algorithm(self._game.dict, self._game._board)
            step = move_game[1]
            car = move_game[0]

            # If the step-size is 0, begin again, else move that car
            if step == 0:
                pass
            else:
                self._game.move(car, step)
                self._count_steps += 1
                self._steps.append((car, step))

>>>>>>> 25ac3e4bad46ff4224d021687e90fbb07e3e4c9a



            


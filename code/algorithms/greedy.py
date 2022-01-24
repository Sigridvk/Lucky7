# from ..classes.rushhour import rushhour

class Greedy():
    """
    """

    def __init__(self, game):
        self._game = game
        self.blocking_car = ""


    def red_car_forward(self):
        
        # Define coordinate right to red car
        column_ = self._game.dict['X']['col'] + 2
        row =  self._game.dict['X']['row']
        
	    # Check if red car can move
        for i in range(column_, self._game.size_board):
            if self._game._board[row][i] == '':
                
                # move the red car
                self._game.move('X', 1)

                column_ += 1

            else:
                self.blocking_car = self._game._board[row][i]
                break


    def run_random_greedy(self):
        pass

            # self._game.dict['X']['column'] = column_


            


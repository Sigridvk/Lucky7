# from ..classes.rushhour import rushhour

class Greedy():
    """
    """

    def __init__(self, game):
        self._game = game


    def red_car_forward(self):
        
        # Define coordinate right to red car
        column_ = self._game.dict['X']['col'] + 2
        row =  self._game.dict['X']['row']
        
	    # Check if red car can move
        if self._game._board[row][column_] == '':
            
            # move the red car
            self._game.move('X', 1)

            # self._game.dict['X']['column'] = column_
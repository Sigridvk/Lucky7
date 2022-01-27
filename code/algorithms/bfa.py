
import copy
import queue
from ..classes.rushhour import rushhour
import re


class Breadth_first():

    def __init__(self, output, game):
        """
        """
        
        self.rushhourgame_init = rushhour(output, game)

        # Initialize list that will contain possible moves
        self._all_moves = []
        
        for key in self.rushhourgame_init.dict:

            if self.rushhourgame_init.dict[key]["orientation"] == 'V':
                self._all_moves.append(str(key) + '1' + 'U')
                self._all_moves.append(str(key) + '1' + 'D')
            
            else:
                self._all_moves.append(str(key) + '1' + 'L')
                self._all_moves.append(str(key) + '1' + 'R')
        
        self._state = ''
        self._game_name = game
        self._output = output
    
    
    def unpack_moves(self):
        """
        """

        splitted_string = []
        n  = 3
        for index in range(0, len(self._state), n):
            splitted_string.append(self._state[index : index + n])

        # print(splitted_string)
        return splitted_string
    
    
    def check_move(self, car, steps):
        """
        Checks whether a move is valid.
        """
        
        # # Define move and append to moves
        # # move = (car, steps)
        # # self.moves.append(move)

        # moves = self.unpack_moves()

        # for i in moves:

        # Horizontal
        if self.dict[car]['orientation'] == 'H':
            
            # Redefine column coordinate vehicle
            self.dict[car]['col'] += steps

        # Vertical
        else:
            # Redefine row coordinate vehicle
            self.dict[car]['row'] -= steps
        
        # self.create_board()
        # self.display_board()



    def run(self):
        """
        """

        depth = 40

        # Waarom wordt queue niet gepakt?
        queue_ = queue.Queue()
        queue_.put("")

        while not queue_.empty():
        
            state = queue_.get()

            self._state = state
            
            # Unpack moves
            self.unpack_moves()

            self.rushhourgame = rushhour(self._output, self._game_name)

            # print(state)

            if len(state) < depth:
                for i in self._all_moves:
                    child = copy.deepcopy(state)
                    child += i
                    queue_.put(child)
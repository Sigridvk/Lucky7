import copy
import queue
from time import sleep
from ..classes.rushhour import rushhour
import algo1


class Breadth_first1():

    def __init__(self, output, game, depth = 4):
        """
        """
        
        self._rushhourgame = rushhour(output, game)
        self._depth = depth
        self._all_moves = []

        self._queue_states = queue.Queue()
        self._board = copy.deepcopy(self._rushhourgame.create_board())
        self._current_board = self._board
        self._queue_states.put({0:self._board})
        
        self._state = self._board

        
    
    def all_moves(self, board):

        for car in self._rushhourgame.dict:
            moves = algo1.check_move(car, self._rushhourgame.dict, board)
            for move in moves:
                move1 = car + str(move)
                self._all_moves.append(move1)
        print(self._all_moves)
        return(self._all_moves)
    
    def run(self):
        self.build_children(self._board)
        # print(self._queue_states.get())

    def get_next_state(self):
        return self._queue.get()

    def build_children(self, board):
        children = self.all_moves(board)
        for child in children:
            car = child[0]
            step = int(child[1:])
            print(car, step)
            self._rushhourgame2 = copy.deepcopy(self._rushhourgame)
            self._rushhourgame2.move(car, step)
            print(self._rushhourgame2._board)
            # self._rushhourgame = copy.deepcopy(self._rushhourgame)
            # print(self._rushhourgame._board)
            # print(self._board)
            self._rushhourgame2.display_board()
            sleep(5)
            self._queue_states.put({child:self._board})


    



# bfa = Breadth_first('test_bfa.csv', 'Rushhour_6x6_1', 1)
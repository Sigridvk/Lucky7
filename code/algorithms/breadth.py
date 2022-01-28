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

        self._queue_states = queue.Queue()
        self._board = copy.deepcopy(self._rushhourgame.create_board())
        self._current_board = self._board
        self._queue_states.put({0:self._rushhourgame.dict})
        
        self._state = self._board

        
    
    def all_moves(self, last_step):
        self._all_moves = []
        if last_step != '0':
            car1 = last_step[0]
            step = int(last_step[1:])
            step = step * -1
            last_step = car1 + str(step)
        board = self._rushhourgame.create_board()
        board = self._rushhourgame._board
        # print(f"Board in all moves: {board}")
        for car in self._rushhourgame.dict:
            moves = algo1.check_move(car, self._rushhourgame.dict, board)
            for move in moves:
                move1 = car + str(move)
                if move1 != last_step:
                    self._all_moves.append(move1)
        # print(f"Possible moves: {self._all_moves}")
        # print()
        return(self._all_moves)
    




    def get_next_state(self):
        # print(self._queue_states.get())
        return self._queue_states.get()

    def build_children(self, last_step):
        # print(f"Board: {dict}")
        children = self.all_moves(last_step)
        self._depth += 1
        print(self._depth)
        for child in children:
            car = child[0]
            step = int(child[1:])
            child1 = car + str(step)
            print(str(last_step)+ '_' +child1)
            # print(car, step)
            self._rushhourgame2 = copy.deepcopy(self._rushhourgame)
            self._rushhourgame2.create_board()
            # self._rushhourgame2.display_board()
            
            self._rushhourgame2.move(car, step)
            self._rushhourgame2._board = copy.deepcopy(self._rushhourgame2.create_board())
            self._rushhourgame.display_board()
            if self._rushhourgame.solved():
                break
            # sleep(0.5)
            self._queue_states.put({child1:self._rushhourgame2.dict})
        
            

    def solved(self):
        if self._rushhourgame.solved():
            print("solved")
            return True

    

    def run(self):

        # for i in range(5):
        while self._queue_states:
            if self.solved():
                break
            state_dict = self.get_next_state()
            # print(f"state dict: {state_dict}")
            # print(f"state_dict {state_dict}")
            all_steps = list(state_dict.keys())[0]
            all_steps = str(all_steps)
            print(f"all steps: {all_steps}")
            all_steps = all_steps.split('_')
            print(all_steps)
            last_step = all_steps[-1]
            state_dict = list(state_dict.values())[0]
            
            
            # state_dict.create_board()
            # print(f"state: {state_dict}")
            self._rushhourgame.dict = state_dict
            # print("Checking if solved")
            # print(self._rushhourgame._board)
            
            self.build_children(last_step)
            






# bfa = Breadth_first('test_bfa.csv', 'Rushhour_6x6_1', 1)
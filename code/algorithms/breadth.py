import copy
import queue
from time import sleep
from ..classes.rushhour import rushhour
import algo1
import csv


class Breadth_first1():

    def __init__(self, output, game, depth = 4):
        """
        """
        self._game = game
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
        print(f"Possible moves: {self._all_moves}")
        # print()
        return(self._all_moves)
    

    def get_next_state(self):
        # print(self._queue_states.get())
        return self._queue_states.get()

    def build_children(self, all_steps):
        lengte = len(all_steps) - 3
        last_step = all_steps[lengte:]
        last_step = last_step[0]
        print(f"Last_step: {last_step}")
        if last_step[0] == '_':
            str1 = ""
            last_step= last_step[1:]
            for i in last_step:
                str1 += i
            last_step = str1
            print(f"Last_Step in if {last_step}")

        children = self.all_moves(last_step)

        self._depth += 1
        # print(self._depth)
        for child in children:
            car = child[0]
            step = int(child[1:])
            child1 = car + str(step)
            print(f"child1 : {child1}")
            listToStr ='_'.join([str(elem) for elem in all_steps])
            print(f"list to str: {listToStr}")
            child2 = listToStr
            child2 += '_' + child1
            print(f"child2: {child2}")
            # print(car, step)
            self._rushhourgame2 = copy.deepcopy(self._rushhourgame)
            self._rushhourgame2.create_board()
            # self._rushhourgame2.display_board()
            self._rushhourgame2._path += child2
            print(self._rushhourgame2._path)
            self._rushhourgame2.move(car, step)
<<<<<<< HEAD
            print(self._rushhourgame2._board)
            # self._rushhourgame = copy.deepcopy(self._rushhourgame)
=======
            # self._rushhourgame2._board = copy.deepcopy(self._rushhourgame2.create_board())
            # self._rushhourgame.display_board()
            # sleep(1)
            if self._rushhourgame.solved():
                print(f"Oplossing: {all_steps}")
                all_steps.append('A-1')
                with open(f'output/bfa/best_solution_{self._game}.csv','w') as out:
                    csv_out=csv.writer(out)
                    csv_out.writerow(['car','move'])
                    for row in all_steps:
                        csv_out.writerow(row)
                break
            # sleep(0.5)
            self._queue_states.put({child2:self._rushhourgame2.dict})
        
            

    def solved(self):
        if self._rushhourgame.solved():
            print("solved")
            return True


    def run(self):
        # path = ""
        all_steps = ""
        # for i in range(15):
        while self._queue_states:
            if self.solved():
                break
            state_dict = self.get_next_state()
            print(f"state dict: {state_dict}")
            # print(f"state_dict {state_dict}")
            all_steps = list(state_dict.keys())[0]
            all_steps = str(all_steps)
            # all_steps += all_steps
            print(f"all steps: {all_steps}")
            all_steps = all_steps.split('_')
            # print(all_steps)
            last_step = all_steps[-1]
            print(f"Last step {last_step}")
            state_dict = list(state_dict.values())[0]
            
            
            # state_dict.create_board()
            # print(f"state: {state_dict}")
            self._rushhourgame.dict = state_dict
            # print("Checking if solved")
>>>>>>> 382ee80cfe69382e9e722478af9eac2561a1cd04
            # print(self._rushhourgame._board)
            
            self.build_children(all_steps)
            # path += last_step
            # print(f"path: {path}")

            






# bfa = Breadth_first('test_bfa.csv', 'Rushhour_6x6_1', 1)
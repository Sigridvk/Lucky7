"""
breadth.py

Programmeertheorie
Sigrid van Klaveren, Vanja Misuric-Ramljak and Luna Ellinger
"""

import copy
import queue
from time import sleep
from ..classes.rushhour import rushhour
import algo1
import csv
# import pandas as pd

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

        # A variable that is used for printing the depth of the search
        self.__depth = 0

        # An empty set to memorize unique boards
        self._unique_boards = ()

    
    def all_moves(self, last_step):
        """
        Checks all moves that can be made from a certain state.
        Returns a list with the moves.
        Takes as parameter last_step so that this step will not be made.
        """

        # Create empty list for moves
        self._all_moves = []

        # Remove the move from the list that has just been made 
        if last_step != '0':
            car1 = last_step[0]
            step = int(last_step[1:])
            step = step * -1
            last_step = car1 + str(step)

        board = self._rushhourgame.create_board()

        # (Heb je het bord niet al door de bovenstaande regel code?)
        board = self._rushhourgame._board

        # For-loop over all cars in dict
        for car in self._rushhourgame.dict:
            moves = algo1.check_move(car, self._rushhourgame.dict, board)
            
            # Append moves found for particular car to the all_moves list
            for move in moves:
                move1 = car + str(move)
                if move1 != last_step:
                    self._all_moves.append(move1)
        
        return(self._all_moves)
    

    def get_next_state(self):
        """
        """
        return self._queue_states.get()


    def build_children(self, all_steps):
        """
        """

        # Get last step that has been made 
        # (Kan misschien later weggehaald worden wanneer we staten op gaan slaan)
        length = len(all_steps) - 3
        last_step = all_steps[length:]
        last_step = last_step[0]

        if last_step[0] == '_':
            str1 = ""
            last_step= last_step[1:]
            for i in last_step:
                str1 += i
            last_step = str1

        # Create children from current state (possible steps)
        children = self.all_moves(last_step)

        # self._depth += 1

        # For-loop over children
        for child in children:
            
            # Define car and step
            car = child[0]
            step = int(child[1:])

            # Current child
            child1 = car + str(step)

            # Join the all_steps with current child
            listToStr ='_'.join([str(elem) for elem in all_steps])
            
            # path_ are all the previous steps
            path_ = listToStr
            path_ += '_' + child1

            # In rushhourgame2 the children (moves) 
            self._rushhourgame2 = copy.deepcopy(self._rushhourgame)

            # 
            self._rushhourgame2._path += path_

            # Moves vehicle by changing the dict
            self._rushhourgame2.move(car, step)

            # Prints depth once arrived at new depth
            if len(all_steps) > self.__depth:
                self.__depth = copy.deepcopy(len(all_steps))
                print(self.__depth)
             
            # Checks whether solution is found
            if self._rushhourgame.solved():
                print(f"Oplossing: {all_steps}")            

                # Write best solution to an output file
                with open(f'output/bfa/best_solution_{self._game}.csv','w') as out:
                    writer = csv.writer(out)
                    writer.writerow(['car','move'])
                    
                    # Remove begin state (0) from list
                    all_steps.remove('0')

                    for element in all_steps:
                        car_ = element[0]
                        step_ = element[1:]
                        writer.writerow([car_, step_])
                break
<<<<<<< HEAD

            # df = pd.read_csv(f'output/bfa/best_solution_{self._game}.csv')
            # df['move'] = df['move'].str.replace('-', '')
            # df.to_csv('cleaned.csv')
                
=======
            
>>>>>>> fc006bddaa6f1160baceed1b7ff9b28d2b8973c5
            # sleep(0.5)
            self._queue_states.put({path_:self._rushhourgame2.dict})
        
            
    def solved(self):
        """
        Checks whether game is solved.
        """

        if self._rushhourgame.solved():
            print("solved")
            return True


    def run(self):
        """
        """

        all_steps = ""

        # 
        while self._queue_states:
            if self.solved():
                break
            
            # Gets next state 
            state_dict = self.get_next_state()

            # Get key of next state (key is the path)
            all_steps = list(state_dict.keys())[0]
            all_steps = str(all_steps)

            # Puts steps seperately in a list 
            all_steps = all_steps.split('_')

            # Get the value (dict) of the next state
            state_dict = list(state_dict.values())[0]

            # Make the 'next_dict' the 'current_dict'
            self._rushhourgame.dict = state_dict
            
            # Create children from current state
            self.build_children(all_steps)

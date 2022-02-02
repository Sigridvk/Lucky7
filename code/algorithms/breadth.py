"""
breadth.py

Programmeertheorie
Sigrid van Klaveren, Vanja Misuric-Ramljak and Luna Ellinger

- Contains the class Breadth_first, which is used to run a breadth first algorithm.
- Class is initialized with a game name
- The class will create a queue with all possible states of the game
"""

import copy
import queue
from ..classes.rushhour import Rushhour
import randomise
import csv

class Breadth_first():

    def __init__(self, game):
        
        # Create two rushhourgame instances
        self._game = game
        self._rushhourgame = Rushhour(game)
        self._rushhourgame2 = Rushhour(game)
        
        # An archive to memorize which states have been visited
        self._archive = set()
        
        # A queue for all the possible states
        self._queue_states = queue.Queue()
        
        # Add the begin board to the queue
        self._queue_states.put({0:self._rushhourgame.dict})
        self._rushhourgame.create_board()
        
        # A variable that is used for printing the depth of the search
        self.__depth = 0

    
    def all_moves(self):
        """
        Checks all moves that can be made from a certain state.
        Returns a list with the moves.
        """

        # Create empty list for moves
        self._all_moves = []

        board = self._rushhourgame.create_board()

        # For-loop over all cars in dict to check how they can move
        for car in self._rushhourgame.dict:
            moves = randomise.check_move(car, self._rushhourgame.dict, board)
            
            # Append moves found for particular car to the all_moves list
            for move in moves:
                move1 = car + str(move)
                self._all_moves.append(move1)
        
        return(self._all_moves)
    

    def get_next_state(self):
        """
        Returns the next state from the queue
        """
        return self._queue_states.get()


    def build_children(self, all_steps):
        """
        Function that creates all child states from a certain state. 
        Appends these children to the queue.
        Gets a list of all steps that have to be taken to get a certain state.
        """

        # Get all possible moves
        children = self.all_moves()

        # Loop over each child to create the state
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

            # Deepcopy the dict of the current state 
            self._rushhourgame2.dict = copy.deepcopy(self._rushhourgame.dict)

            self._rushhourgame2._path += path_

            # Moves vehicle by changing the dict
            self._rushhourgame2.move(car, step)
            self._rushhourgame2.create_board()

            # Saves the depth once arrived at new depth
            if len(all_steps) > self.__depth:
                self.__depth = copy.deepcopy(len(all_steps))

            # Checks whether solution is found
            if self._rushhourgame.solved():

                # Write best solution to an output file
                with open(f'output/breadth/best_solution_{self._game}.csv','w') as out:
                    writer = csv.writer(out)
                    writer.writerow(['car','move'])
                    
                    # Remove begin state (0) from list
                    all_steps.remove('0')

                    for element in all_steps:
                        car_ = element[0]
                        step_ = element[1:]
                        writer.writerow([car_, step_])
                break      
            
            # Create a string of the current state
            bord = board_to_string(self._rushhourgame2)
        
            # Check if this board is already in the archive, if not add it to the queue
            if bord not in self._archive:
                self._queue_states.put({path_:self._rushhourgame2.dict})
                self._archive.add(bord)
        
            
    def solved(self):
        """
        Checks whether game is solved.
        """
        self._rushhourgame.create_board()
        if self._rushhourgame.solved():
            return True


    def run(self):
        """
        Runs the Breadth First algorithm
        """

        # Run the algorithm as long as the queue is not empty
        while self._queue_states:
            if self.solved():
                break
            
            # Gets next state 
            state_dict = self.get_next_state()

            # Get all the steps that have been taken so far
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


def board_to_string(game):
    """
    Function to create a string of a certain board.
    """
    bord = ""
    for i in range(len(game._board)):
        for j in range(len(game._board)):
            if game._board[i][j] == '':
                game._board[i][j] = '.'
            bord += game._board[i][j]
    return (bord)

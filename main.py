"""
main.py

Programmeertheorie
Sigrid van Klaveren, Vanja Misuric-Ramljak and Luna Ellinger

- Contains the main loop that calls an algorithm that solves the game RushHour.

Usage: python3 rushhour.py -g GAME -a ALGORITHM [-n NUMER_OF_RUNS] 
Algorithms: random, breadth, greedy1, greedy2
"""

import argparse
from random import random
import time
from sys import argv
from code import save_data
from code.algorithms import randomise
from code.classes.rushhour import Rushhour
from code.algorithms.greedy import Greedy
from code.algorithms.breadth import Breadth_first


# Global variable for the total steps per solved game, game with smallest amount of steps, steps from the smallest game
solved_games = []
smallest_amount_steps = None
steps_from_smallest_game = []


# WORDT NOG NIET GEBRUIKT
def save_steps_smallest_game(smallest_amount_steps, steps_from_smallest_game, stepcount):
    """
    """

    # Check whether the current game is run in the least amount of steps
    if smallest_amount_steps == None or smallest_amount_steps > stepcount:
        
        # Redefine smallest_amount_steps and save the steps from this game
        smallest_amount_steps = stepcount
        steps_from_smallest_game = rushhourgame.moves


if __name__ == "__main__":

    # Create a command line argument parser
    parser = argparse.ArgumentParser(description='Solve a rushhour game')
    parser.add_argument("-g", "--game", type=str, help="gamefile name", required=True)
    parser.add_argument("-a","--algorithm", type=str, help="choose algorithm", required=True)
    parser.add_argument("-n","--runs", type=int, default=1, help="number of runs")

    # Parse the command line arguments
    args = parser.parse_args()

    # Check command line arguments
    if len(argv) not in [5, 7]:
        print(len(argv))
        print("Usage: python3 rmain.py -g GAME -a ALGORITHM [-n NUMER_OF_RUNS]")
        exit(1)

    # Run random
    if args.algorithm == 'random':
        start_time = time.time()

        random = randomise.run_algorithm(args.game, args.runs)

        end_time = time.time()
        time_passed = end_time - start_time

        save_data.save_data(random[0], random[1], args.game, args.algorithm)

    # Run greedy1
    elif args.algorithm == 'greedy1':

        # For-loop in range of runs
        for run in range(args.runs):

            # Initialize instance of class rushhour
            rushhourgame = Rushhour(args.game)

            # Initialize greedy class
            game_greedy1 = Greedy(rushhourgame)

            # run random greedy algorithm
            game_greedy1.run_random_greedy1()

            # Check whether the current game is run in the least amount of steps
            if smallest_amount_steps == None or smallest_amount_steps > game_greedy1._count_steps:
                
                # Redefine smallest_amount_steps and save the steps from this game
                smallest_amount_steps = game_greedy1._count_steps
                steps_from_smallest_game = rushhourgame.moves
            
            # save_steps_smallest_game(smallest_amount_steps, steps_from_smallest_game,  game_greedy1._count_steps)

            # Add total steps of solved game to list
            solved_games.append(game_greedy1._count_steps)

        # Save data to output files
        save_data.save_data(steps_from_smallest_game, solved_games, args.game, args.algorithm)

    # Run greedy2 
    elif args.algorithm == 'greedy2':
        for run in range(args.runs):

            # initialize instance of class rushhour
            rushhourgame = Rushhour(args.game)

            game_greedy2 = Greedy(rushhourgame)

            # run random greedy algorithm
            game_greedy2.run_random_greedy2()

            # Check whether the current game is run in the least amount of steps
            if smallest_amount_steps == None or smallest_amount_steps > game_greedy2._count_steps:
                
                # Redefine smallest_amount_steps and save the steps from this game
                smallest_amount_steps = game_greedy2._count_steps
                steps_from_smallest_game = rushhourgame.moves

            # add total steps of solved game to list
            solved_games.append(game_greedy2._count_steps)
        
        # Save data to output files
        save_data.save_data(steps_from_smallest_game, solved_games, args.game, args.algorithm)

    # Run breadth-first-search algorithm
    elif args.algorithm == 'breadth':
        
        # initialize instance of class rushhour
        rushhourgame = Rushhour(args.game)

        # Initialize breadth first algo class
        game_breadth = Breadth_first(args.game,0)

        # Run algorithm
        game_breadth.run()

    else:
        print("Usage: python3 rushhour.py -g GAME -o OUTPUT -a ALGORITHM [-n NUMER_OF_RUNS]")

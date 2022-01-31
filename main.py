"""
main.py

Programmeertheorie
Sigrid van Klaveren, Vanja Misuric-Ramljak and Luna Ellinger

- Contains the main loop that calls an algorithm that solves the game RushHour.

Usage: python3 rushhour.py -g GAME -o OUTPUT -a ALGORITHM [-n NUMER_OF_RUNS]
"""

import argparse
from random import random
import time
import datetime
from sys import argv
from code import save_data
from code.algorithms import algo1
from code.classes import rushhour
from code.classes.rushhour import rushhour
from code.algorithms.greedy import Greedy
# from code.algorithms.bfa import Breadth_first
from code.algorithms.breadth import Breadth_first1
from code.algorithms.breadth_first import Breadth_first2


# Global variable for the total steps per solved game, game with smallest amount of steps, steps from the smallest game
solved_games = []
smallest_amount_steps = None
steps_from_smallest_game = []

if __name__ == "__main__":

    print(datetime.datetime.now())

    # Create a command line argument parser
    parser = argparse.ArgumentParser(description='Solve a rushhour game')
    parser.add_argument("-g", "--game", type=str, help="gamefile name", required=True)
    parser.add_argument("-o", "--output", help="output file (csv)", required=True)
    parser.add_argument("-a","--algorithm", type=str, help="choose algorithm", required=True)
    parser.add_argument("-n","--runs", type=int, default=1, help="number of runs")

    # Parse the command line arguments
    args = parser.parse_args()

    # print(len(argv))
    
    # Check command line arguments
    if len(argv) not in [7,9]:
        print(len(argv))
        print("Usage: python3 rushhour.py -g GAME -o OUTPUT -a ALGORITHM [-n NUMER_OF_RUNS]")
        exit(1)

    if args.algorithm == 'random':
        start_time = time.time()

        random = algo1.run_algorithm(args.output, args.game, args.runs, smallest_amount_steps, steps_from_smallest_game, solved_games)

        end_time = time.time()
        time_passed = end_time - start_time

        save_data.save_data(random[0], random[1], args.game, args.algorithm)

    elif args.algorithm == 'greedy1':
        for i in range(args.runs):

            # initialize instance of class rushhour
            rushhourgame = rushhour(args.output, args.game)

            game_greedy1 = Greedy(rushhourgame)
            # if (i % 50) == 0:
            #     print(i)

            # # initialize instance of class rushhour
            # rushhourgame = rushhour(args.output, args.game)

            # run random greedy algorithm
            game_greedy1.run_random_greedy1()

            # Check whether the current game is run in the least amount of steps
            if smallest_amount_steps == None or smallest_amount_steps > game_greedy1._count_steps:
                
                # Redefine smallest_amount_steps and save the steps from this game
                smallest_amount_steps = game_greedy1._count_steps
                steps_from_smallest_game = rushhourgame.moves
                # print(game_greedy1._count_steps)

            # add total steps of solved game to list
            solved_games.append(game_greedy1._count_steps)

        save_data.save_data(steps_from_smallest_game, solved_games, args.game, args.algorithm)


    elif args.algorithm == 'greedy2':
        for i in range(args.runs):

            # initialize instance of class rushhour
            rushhourgame = rushhour(args.output, args.game)

            game_greedy2 = Greedy(rushhourgame)
            # if (i % 50) == 0:
            #     print(i)

            # # initialize instance of class rushhour
            # rushhourgame = rushhour(args.output, args.game)

            # run random greedy algorithm
            game_greedy2.run_random_greedy2()

            # Check whether the current game is run in the least amount of steps
            if smallest_amount_steps == None or smallest_amount_steps > game_greedy2._count_steps:
                
                # Redefine smallest_amount_steps and save the steps from this game
                smallest_amount_steps = game_greedy2._count_steps
                steps_from_smallest_game = rushhourgame.moves
                # print(game_greedy2._count_steps)

            # add total steps of solved game to list
            solved_games.append(game_greedy2._count_steps)
        
        save_data.save_data(steps_from_smallest_game, solved_games, args.game, args.algorithm)


    elif args.algorithm == 'breadth':
        # initialize instance of class rushhour
        rushhourgame = rushhour(args.output, args.game)

        game_breadth = Breadth_first1(args.output, args.game,0)

        game_breadth.run()

    else:
        print("Usage: python3 rushhour.py -g GAME -o OUTPUT -a ALGORITHM [-n NUMER_OF_RUNS]")


    # start_time = time.time()

    # initialize instance of class rushhour
    # rushhourgame = rushhour(args.output, args.game)

    # print(args.runs)

    # random = algo1.run_algorithm(args.output, args.game, args.runs, smallest_amount_steps, steps_from_smallest_game, solved_games)

    #     # initialize instance of class Greedy --> MISSCHIEN WILLEN WE DIT DUS ELKE KEER EEN ANDERE INSTANTIE MAKEN, NU OVERSCHRIJFT HIJ HEM
    #     game_algo1 = Greedy(rushhourgame)
        # if (i % 500) == 0:
        #     print(i)

    # # RANDOM GREEDY
    # # # Run algorithm multiple times
    # for i in range(args.runs):

    # #     # initialize instance of class rushhour
    # #     rushhourgame = rushhour(args.output, args.game)


    # #     # initialize instance of class Greedy --> MISSCHIEN WILLEN WE DIT DUS ELKE KEER EEN ANDERE INSTANTIE MAKEN, NU OVERSCHRIJFT HIJ HEM
    # #     game_greedy2 = Greedy(rushhourgame)
    # #     if (i % 50) == 0:
    # #         print(i)

    #     # initialize instance of class rushhour
    #     rushhourgame = rushhour(args.output, args.game)


    # #     # run random greedy algorithm
    # #     game_greedy2.run_random_greedy()

    # #     # Check whether the current game is run in the least amount of steps
    # #     if smallest_amount_steps == None or smallest_amount_steps > game_greedy2._count_steps:
            
    # #         # Redefine smallest_amount_steps and save the steps from this game
    # #         smallest_amount_steps = game_greedy2._count_steps
    # #         steps_from_smallest_game = rushhourgame.moves

    # #     # add total steps of solved game to list
    # #     solved_games.append(game_greedy2._count_steps)

    # # BREADTH FIRST
    # # initialize instance of class rushhour
    # # rushhourgame = rushhour(args.output, args.game)

    # # game_bfa = Breadth_first(args.output, args.game)
    # game_breadth = Breadth_first1(args.output, args.game,0)
    # game_breadth.run()

    # game_bfa.run()

    # end_time = time.time()
    # time_passed = end_time - start_time
    # print(time_passed)
    
    # print()

    # # Show how much time it took to run the algorithm
    # print(f"It took {time_passed} seconds to solve {args.game} {args.runs} times.")

    # # Call save_data to write data to output file
    # save_data.save_data(random[0], random[1], time_passed, args.game)

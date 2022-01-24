"""
main.py

Programmeertheorie
Sigrid van Klaveren, Vanja Misuric-Ramljak and Luna Ellinger

- Contains the main loop that calls an algorithm that solves the game RushHour.

Usage: python3 rushhour.py -g GAME -o OUTPUT [-n NUMER_OF_RUNS]
"""

import argparse
# from code.algorithms import algo1
import time
from sys import argv
from code import save_data
from code.algorithms import algo1
from code.classes.rushhour import rushhour
from code.algorithms.greedy import Greedy

# Global variable for the total steps per solved game, game with smallest amount of steps, steps from the smallest game
solved_games = []
smallest_amount_steps = None
steps_from_smallest_game = []

if __name__ == "__main__":

    # print(datetime.datetime.now())

    # Create a command line argument parser
    parser = argparse.ArgumentParser(description='Solve a rushhour game')
    parser.add_argument("-g", "--game", type=str, help="gamefile name", required=True)
    parser.add_argument("-o", "--output", help="output file (csv)", required=True)
    parser.add_argument("-n","--runs", type=int, default=1, help="number of runs")

    # Parse the command line arguments
    args = parser.parse_args()

    # Check command line arguments
    if len(argv) not in [5,7]:
        print(len(argv))
        print("Usage: python3 rushhour.py -g GAME -o OUTPUT [-n NUMER_OF_RUNS]")
        exit(1)
    
    start_time = time.time()

    rushhourgame = rushhour(args.output, args.game)

    # # Run algorithm one (random)
    # game_algo1 = algo1.run_algorithm(args.runs, args.game, args.output, smallest_amount_steps, steps_from_smallest_game, solved_games)
    # # game_algo1 = algo1.run_algorithm(args.runs, args.game)

    rushhourgame.move('A', -1)
    rushhourgame.create_board()
    rushhourgame.display_board(rushhourgame._board)

    rushhourgame.move('C', -1)
    rushhourgame.create_board()
    rushhourgame.display_board(rushhourgame._board)

    rushhourgame.move('G', 2)
    rushhourgame.create_board()
    rushhourgame.display_board(rushhourgame._board)

    run1 = Greedy(rushhourgame)
    run1.red_car_forward()
    rushhourgame.create_board()
    rushhourgame.display_board(rushhourgame._board)


    end_time = time.time()

    # time_passed = end_time - start_time
    # steps_from_smallest_game = game_algo1[0]
    # solved_games = game_algo1[1]
    
    # Show how much time it took to run the algorithm
    print(f"It took {time_passed} seconds to solve {args.game} {args.runs} times.")
    
    # Call save_data to write data to output file
    # save_data.save_data(steps_from_smallest_game, solved_games, time_passed, args.output)
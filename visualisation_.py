import sys
# from draw import draw
import turtle
import argparse
import csv

from code.classes.rushhour import rushhour


if __name__ == "__main__":

    # argparse (roep het programma aan met de juiste moves)
    # Create a command line argument parser
    parser = argparse.ArgumentParser(description='Solve a rushhour game with defined steps')
    # parser.add_argument("-g", "--game", type=str, help="gamefile name", required=True)
    # parser.add_argument("-i", "--input", help="file with steps (csv)", required=True)

    # Parse the command line arguments
    args = parser.parse_args()

    rushhourgame = rushhour("test.csv", "Rushhour6x6_1")

    reader = csv.reader(open("output_moves.csv"))
    
    rushhourgame.create_board
    rushhourgame.display_board()

    # Load steps into a dictionary 
    for row in list(reader)[1:]:
        car = row[0]
        step = int(row[1])

        rushhourgame.move(car, step)
        rushhourgame.create_board()
        rushhourgame.display_board()



import sys
from draw import draw
import turtle
import argparse
import csv

sys.path.append("../")

from classes.rushhour import rushhour

# import pathlib

# path = pathlib.Path().resolve()
# path = str(path)
# path = path.strip("visualisation")
# path = path + "classes"

# import ..classes.rushhour

# print("hello")
# print(path)


if __name__ == "__main__":

    # rushhourgame = rushhour("test.csv", "Rushhour6x6_1")

    # argparse (roep het programma aan met de juiste moves)
    # Create a command line argument parser
    parser = argparse.ArgumentParser(description='Solve a rushhour game with defined steps')
    parser.add_argument("-g", "--game", type=str, help="gamefile name", required=True)
    parser.add_argument("-i", "--input", help="file with steps (csv)", required=True)

    # Parse the command line arguments
    args = parser.parse_args()
    
    reader = csv.reader(open(args.input))
    
    # Importeer lijst met moves en zet in dict
    dict = {}

    # Load steps into a dictionary 
    for row in list(reader)[1:]:
        car_name = row[0]
        dict[car_name] = row[1]
    
    print(dict)


    # Maak er een dictionary van

    # Creeer board

    # Maak een move

    # Display board

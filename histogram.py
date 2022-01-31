"""
histogram.py

Programmeertheorie
Sigrid van Klaveren, Vanja Misuric-Ramljak and Luna Ellinger
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import argparse

def addlabels(y):
    """
    """

    for i in range(9):
        plt.text(i, y[i], y[i], ha = 'center')


def bar_chart_large_range(dataframe):
    """
    """
    pass


def bar_chart_small_range(dataframe):
    """
    """
    pass


def histogram(input_file, output_file):
    """
    """

    path_to_file = "output/algo_1/"

    input = path_to_file + input_file

    # define game name
    game_name = input_file[13:]

    # Create dataframe from 
<<<<<<< HEAD
    df = pd.read_csv(input_file, header=None)
    # Dataframe sorteren
    df.sort_values(
        [0],
        ascending=True,
        inplace=True  # sortering van het originele dataframe aanpassen
)

    print(df.max())
    df['bins'] = pd.cut(df[0], bins=np.linspace(0, (df.max()[0])/4, 10).astype(int))
    # print(df)
=======
    df = pd.read_csv(input, header=None)
    
    # Sort dataframe
    df.sort_values([0],ascending = True, inplace = True)
    
    # Create bins
    df['bins'] = pd.cut(df[0], bins=np.linspace(0, (df.max()[0]), 10).astype(int))
>>>>>>> 7833a3dd31b95516addf07854cbdb662f5cc8841
    bin_counts = df['bins'].value_counts().sort_index()


    plt.figure(figsize = (10, 5))
    bin_counts.plot.bar()
    bin_counts = bin_counts.tolist()

    # function to add value labels
    addlabels(bin_counts)
    
    # Label plot
    plt.xlabel("Steps"), plt.ylabel("Frequency"), plt.title(f"Frequency of Steps per Game {game_name}")

    i = 0
    
    # Give new file name is file name already exists
    # ---- Dit heeft niet veel zin want nu wordt de 1 overschreven
    if os.path.exists('output/graphs/graph.png'):
        i += 1
        plt.savefig(f'output/graphs/{game_name}_{i}.png', bbox_inches = 'tight')

    # ----- Wat gebeurt hier? Waarom twee keer savefig?
    else:
        plt.savefig('output/graphs/graph.png')
        plt.savefig(f'output/graphs/{game_name}.png', bbox_inches = 'tight')

    
    # Define mean and median
    data = {'mean': [df[0].mean()], 'median': [df[0].median()], "shortest_route": [df[0].min()], "longest_route": [df[0].max()]}
    df2 = pd.DataFrame(data)

    # Write mean and median to an outputfile (dit moet anders)
    df2.to_csv(f"output/algo_1/run_information_{game_name}.csv", index=False)


if __name__ == "__main__":

    # Create a command line argument parser
    parser = argparse.ArgumentParser(description='Solve a rushhour game')
    parser.add_argument("-i", "--input", help="output file (csv)", required=True)
    parser.add_argument("-o", "--output", help="output file (csv)", required=True)

    # Parse the command line arguments
    args = parser.parse_args()

    # Check command line arguments
    if len(argv) not in range(3):
        print(len(argv))
        print("Usage: python3 histogram.py -i INPUT -o OUTPUT")
        exit(1)

    # path_to_file = "output"

    histogram(args.input, args.output)

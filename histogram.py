"""
histogram.py

Programmeertheorie
Sigrid van Klaveren, Vanja Misuric-Ramljak and Luna Ellinger

- Contains a program that creates two kinds of barcharts with a varying bin range and a file with the game information
from a file that contains the steps in which the rushhour game is solved per run. 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import argparse
from sys import argv

def addlabels(y):
    """
    Takes as parameter the labels.
    Adds labels to the bars of the chart.
    """

    for i in range(9):
        plt.text(i, y[i], y[i], ha = 'center')


def run_information(df, path, algorithm):
    """
    Takes the dataframe with the amount of steps per game and the path to the directory as parameters.
    Writes the mean, median, minimum and maximum amount of steps to an output file (csv).
    """

    # Define mean and median
    data = {'mean': [df[0].mean()], 'median': [df[0].median()], "shortest_route": [df[0].min()], "longest_route": [df[0].max()]}
    df2 = pd.DataFrame(data)

    # Write mean and median to an outputfile (dit moet anders)
    df2.to_csv(f"{path}/run_information_{algorithm}_{game_name}.csv", index=False)


def bar_chart_large_range(df, game_name, path, algorithm):
    """
    Takes the dataframe with the amount of steps per game. the game name and the path to the directory as parameters.
    Creates a bar chart with a large range of bins to an output file (png).
    """
    
    # Create bins
    df['bins'] = pd.cut(df[0], bins=np.linspace(0, (df.max()[0]), 10).astype(int))
    bin_counts = df['bins'].value_counts().sort_index()

    # plot figure
    plt.figure(figsize = (10, 5))
    bin_counts.plot.bar()
    bin_counts = bin_counts.tolist()

    # function to add value labels
    addlabels(bin_counts)
    
    # Label plot
    plt.xlabel("Steps"), plt.ylabel("Frequency"), plt.title(f"Frequency of Steps per Game - {game_name}")

    # Write figure to an output file
    plt.savefig(f'{path}/large_range_bins_{algorithm}_{game_name}.png', bbox_inches = 'tight')


def bar_chart_small_range(df, game_name, path, algorithm):
    """
    takes the dataframe with the amount of steps per game, the name of the algorithm, the game name 
    and the path to the directory as parameters.
    Creates a bar chart with a large range of bins to an output file (png).
    """

    # Create bins
    df['bins'] = pd.cut(df[0], bins=np.linspace(0, (df.max()[0])/4, 10).astype(int))
    bin_counts = df['bins'].value_counts().sort_index()

    plt.figure(figsize = (10, 5))
    bin_counts.plot.bar()
    bin_counts = bin_counts.tolist()

    # function to add value labels
    addlabels(bin_counts)
    
    # Label plot
    plt.xlabel("Steps"), plt.ylabel("Frequency"), plt.title(f"Frequency of Steps per Game - {game_name}")

    # Write figure to an output file
    plt.savefig(f'{path}/small_range_bins_{algorithm}_{game_name}.png', bbox_inches = 'tight')


def write_info(input_file, algorithm, game_name, path):
    """
    takes the dataframe with the amount of steps per game, the game name, the name of the algorithm
    and the path to the directory as parameters.
    Creates a bar chart with a large range of bins to an output file (png).
    """

    # ------ Dit moet worden aangepast 
    path_to_file = f"output/{algorithm}/"
    input = path_to_file + input_file

    # Create dataframe from 
    df = pd.read_csv(input, header=None)
    
    # Sort dataframe
    df.sort_values([0],ascending = True, inplace = True)

    # Create barchart with large range bins and save chart
    bar_chart_large_range(df, game_name, path, algorithm)

    # Create barchart with small range bins and save chart
    bar_chart_small_range(df, game_name, path, algorithm)

    # Write information of run to an output file
    run_information(df, path, algorithm)


if __name__ == "__main__":

    # Create a command line argument parser
    parser = argparse.ArgumentParser(description='Solve a rushhour game')
    parser.add_argument("-i", "--input", help="input file (csv)", required=True)
    parser.add_argument("-a", "--algo", help="algorithm", required=True)

    # Parse the command line arguments
    args = parser.parse_args()

    # Check command line arguments
    if len(argv) < 4:
        print(len(argv))
        print("Usage: python3 histogram.py -i INPUT -a ALGO")
        print("ALGORITHM is either 'breadth', 'random', 'greedy1' or 'greedy2'")
        exit(1)
    
    # input = args.input
    # index_R = input.find('R')
    # game_name = args.input[index_R:]

    # # define game name
    game_name = args.input[13:]
    game_name = game_name.strip(".csv")

    # Create directory for game
    directory = f"{game_name} - {args.algo}"
    parent_dir = "output/"
    path = os.path.join(parent_dir, directory) 

    # Only create the directory if it does not yet exist
    try:
        os.mkdir(path)
    except FileExistsError:
        pass

    write_info(args.input, args.algo, game_name, path)

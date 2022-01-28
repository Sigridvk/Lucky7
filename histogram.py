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


def histogram(input_file):
    """
    """

    # Create dataframe from 
    df = pd.read_csv(input_file, header=None)
    
    # Sort dataframe
    df.sort_values([0],ascending = True, inplace = True)
    
    # Create bins
    df['bins'] = pd.cut(df[0], bins=np.linspace(0, (df.max()[0]), 10).astype(int))
    bin_counts = df['bins'].value_counts().sort_index()
    # print(bin_counts)

    # print 
    plt.figure(figsize = (10, 5))
    bin_counts.plot.bar()
    bin_counts = bin_counts.tolist()

    # function to add value labels
    addlabels(bin_counts)
    
    # 
    plt.xlabel("Steps"), plt.ylabel("Frequency"), plt.title("Frequency of Steps per Game")

    i = 0 
    if os.path.exists('output/graphs2/graph.png'):
        i += 1
        plt.savefig(f'output/graphs2/9x9_MET_graph_{i}.png', bbox_inches = 'tight')

    else:
        plt.savefig('output/graphs/graph.png')
        plt.savefig('output/graphs2/9x9_MET_graph.png', bbox_inches = 'tight')

    # plt.savefig('output/graphs/graph_', bbox_inches = 'tight')
    # plt.show()
    
    data = {'mean': [df[0].mean()], 'median': [df[0].median()]}
    df2 = pd.DataFrame(data)
    df2.to_csv("output/algo_1/test_mean_and_median_6x6rodeauto.csv", index=False)

    d = {"shortest_route": [df[0].min()], "longest_route": [df[0].max()]}
    df3 = pd.DataFrame(data = d)
    df3.to_csv("output/algo_1/test_shortest_route3_6x6rodeauto.csv", index=False)


if __name__ == "__main__":

    # Create a command line argument parser
    parser = argparse.ArgumentParser(description='Solve a rushhour game')
    parser.add_argument("-o", "--input", help="input file (csv)", required=True)

    # Parse the command line arguments
    args = parser.parse_args()

    # Check command line arguments
    if len(argv) not in range(3):
        print(len(argv))
        print("Usage: python3 histogram.py -o INPUT")
        exit(1)

    histogram("output/algo_1/test_6x6METrodeauto.csv")

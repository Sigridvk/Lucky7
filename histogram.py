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
    # Dataframe sorteren
    df.sort_values(
        [0],
        ascending=True,
        inplace=True  # sortering van het originele dataframe aanpassen
)

    print(df.max())
    df['bins'] = pd.cut(df[0], bins=np.linspace(0, (df.max()[0])/4, 10).astype(int))
    # print(df)
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
<<<<<<< HEAD
<<<<<<< HEAD
        plt.savefig(f'output/graphs2/9x9_MET_graph_{i}.png', bbox_inches = 'tight')

    else:
        plt.savefig('output/graphs/graph.png')
=======
<<<<<<< HEAD
        plt.savefig(f'output/graphs/graph_{i}.png', bbox_inches = 'tight')
    else:
        plt.savefig('output/graphs/graph.png', bbox_inches = 'tight')
=======
        plt.savefig(f'output/graphs2/9x9_MET_graph_{i}.png', bbox_inches = 'tight')
>>>>>>> 719c57acc05376afe47b10795e789ad6564587a8
=======
        plt.savefig(f'output/graphs2/12x12_ZONDER_graph_{i}.png', bbox_inches = 'tight')
>>>>>>> 860164dffd31cce9988fb2b0b757a43ef64d222d
    else:
>>>>>>> 382ee80cfe69382e9e722478af9eac2561a1cd04
        plt.savefig('output/graphs2/9x9_MET_graph.png', bbox_inches = 'tight')
>>>>>>> c1ff6a3e115ca4179ad6569df76a7f1aab88ca05

    # plt.savefig('output/graphs/graph_', bbox_inches = 'tight')
    # plt.show()
<<<<<<< HEAD
    
=======


>>>>>>> 382ee80cfe69382e9e722478af9eac2561a1cd04
    data = {'mean': [df[0].mean()], 'median': [df[0].median()]}
    df2 = pd.DataFrame(data)
<<<<<<< HEAD
<<<<<<< HEAD
    df2.to_csv("output/algo_1/test_mean_and_median_forward_9x9.csv", index=False)
=======
    df2.to_csv("output/algo_1/test_mean_and_median_6x6rodeauto.csv", index=False)
>>>>>>> 3681b41e11098d004b12613bebda0c2a9b67717c
=======
    df2.to_csv("output/algo_1/test_mean_and_median_12x12_ZONDER.csv", index=False)
>>>>>>> 860164dffd31cce9988fb2b0b757a43ef64d222d

<<<<<<< HEAD
    d = {"shortest_route": [df[0].min()], 'longest_route': [df[0].max()]}
=======
    d = {"shortest_route": [df[0].min()], "longest_route": [df[0].max()]}
>>>>>>> c1ff6a3e115ca4179ad6569df76a7f1aab88ca05
    df3 = pd.DataFrame(data = d)
<<<<<<< HEAD
<<<<<<< HEAD
    df3.to_csv("output/algo_1/test_shortest_route_forward_9x9.csv", index=False)

histogram("output/algo_1/test2.csv")
=======
    df3.to_csv("output/algo_1/test_shortest_route3_6x6rodeauto.csv", index=False)

histogram("output/algo_1/test_6x6METrodeauto.csv")
>>>>>>> 3681b41e11098d004b12613bebda0c2a9b67717c
=======
    df3.to_csv("output/algo_1/test_shortest_route3_12x12_ZONDER.csv", index=False)

<<<<<<< HEAD

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
=======
histogram("output/algo_1/ZONDER_algo2_12x12_7_1000times.csv")
<<<<<<< HEAD
>>>>>>> 382ee80cfe69382e9e722478af9eac2561a1cd04
=======
>>>>>>> 860164dffd31cce9988fb2b0b757a43ef64d222d
>>>>>>> 719c57acc05376afe47b10795e789ad6564587a8

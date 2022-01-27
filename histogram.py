from itertools import count
from matplotlib.image import BboxImage
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import os

def addlabels(y):
    for i in range(9):
        plt.text(i, y[i], y[i], ha = 'center')


def histogram(input_file):
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
    print(bin_counts)

    plt.figure(figsize = (10, 5))
    
    bin_counts.plot.bar()

    bin_counts = bin_counts.tolist()

    # function to add value labels
    addlabels(bin_counts)
    
    plt.xlabel("Steps"), plt.ylabel("Frequency"), plt.title("Frequency of Steps per Game")

    i = 0 
    if os.path.exists('output/graphs2/graph.png'):
        i += 1
<<<<<<< HEAD
<<<<<<< HEAD
        plt.savefig(f'output/graphs/graph_{i}.png', bbox_inches = 'tight')
    else:
        plt.savefig('output/graphs/graph.png', bbox_inches = 'tight')
=======
        plt.savefig(f'output/graphs2/9x9_MET_graph_{i}.png', bbox_inches = 'tight')
=======
        plt.savefig(f'output/graphs2/12x12_ZONDER_graph_{i}.png', bbox_inches = 'tight')
>>>>>>> 860164dffd31cce9988fb2b0b757a43ef64d222d
    else:
        plt.savefig('output/graphs2/9x9_MET_graph.png', bbox_inches = 'tight')
>>>>>>> c1ff6a3e115ca4179ad6569df76a7f1aab88ca05

    # plt.savefig('output/graphs/graph_', bbox_inches = 'tight')
    # plt.show()


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

histogram("output/algo_1/ZONDER_algo2_12x12_7_1000times.csv")
>>>>>>> 860164dffd31cce9988fb2b0b757a43ef64d222d

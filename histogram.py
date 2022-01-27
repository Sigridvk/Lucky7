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
    df['bins'] = pd.cut(df[0], bins=np.linspace(0, (df.max()[0]), 10).astype(int))
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
    if os.path.exists('output/graphs/graph.png'):
        i += 1
        plt.savefig(f'output/graphs/graph_{i}.png')
    else:
        plt.savefig('output/graphs/graph.png'

    data = {'mean': [df[0].mean()], 'median': [df[0].median()]}
    df2 = pd.DataFrame(data)
    df2.to_csv("output/algo_1/test_mean_and_median_6x6rodeauto.csv", index=False)

    d = {"shortest_route": [df[0].min()]}
    df3 = pd.DataFrame(data = d)
    df3.to_csv("output/algo_1/test_shortest_route3_6x6rodeauto.csv", index=False)

histogram("output/algo_1/test_6x6METrodeauto.csv")

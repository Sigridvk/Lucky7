from itertools import count
from matplotlib.image import BboxImage
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    plt.savefig('output/graphs/graph_9x9_4_10000n_5', bbox_inches = 'tight')
    # plt.show()

histogram("output/test_9x9_4_10000n_1.csv")
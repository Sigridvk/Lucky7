from matplotlib.image import BboxImage
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def histogram(input_file):
    df = pd.read_csv(input_file, header=None)
    # Dataframe sorteren
    df.sort_values(
        [0],
        ascending=True,
        inplace=True  # sortering van het originele dataframe aanpassen
)
    print(df.max())
    df['bins'] = pd.cut(df[0], bins=np.linspace(0, df.max()[0], 10).astype(int))
    print(df)
    bin_counts = df['bins'].value_counts().sort_index()
    print(bin_counts)

    graph1 = bin_counts.plot.bar()
    
    plt.xlabel("Steps"), plt.ylabel("Frequency"), plt.title("Frequency of Steps per Game")
    plt.savefig('/Users/sigridvanklaveren/Documenten/Uva minor programmeren/Programmeertheorie/Lucky7/output/graphs/graph1', bbox_inches = 'tight')
    # plt.show()

histogram("output/test3.csv")
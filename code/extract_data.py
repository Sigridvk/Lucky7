import pandas as pd

def extract_data(inputfile):
    df = pd.read_csv(inputfile, header=None)
    # Dataframe sorteren
    df.sort_values(
        [0],
        ascending=True,
        inplace=True  # sortering van het originele dataframe aanpassen
        )
    
    print(df)
    print(f"mean: {df.mean()}")
    print(f"median: {df.median()}")
    print(f"min_value: {df.min()}")
    print(f"max_value: {df.max()}")

extract_data("output/output_6x6_10000.csv")


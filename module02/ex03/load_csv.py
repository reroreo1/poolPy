import pandas as pd

def load(path: str)-> pd.DataFrame:
    df = pd.read_csv(path)
    print("dimensions of this dataset are : ",df.shape)
    return df

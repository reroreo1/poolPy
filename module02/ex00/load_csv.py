import pandas as pd
import matplotlib.pyplot as plt

def load(path: str)-> pd.DataFrame:
    df = pd.read_csv(path)
    print("dimensions of this dataset are : ",df.shape)
    # Plotting
    # print(df)
    return df

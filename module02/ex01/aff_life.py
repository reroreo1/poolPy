import pandas as pd
import matplotlib.pyplot as plt

def aff_life(df: pd.DataFrame):
    df.set_index("country", inplace = True)
    df = df.loc['Morocco']
    plt.figure(figsize=(10, 8))
    plt.plot(df)
    plt.title('Life Expectancy Over Time for Morocco')
    plt.xlabel('Year')
    years_to_show = [str(year) for year in range(1800, 2101, 40)]
    plt.xticks(years_to_show, rotation=0)
    plt.ylabel('Life Expectancy')
    plt.show()
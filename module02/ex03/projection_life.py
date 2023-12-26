import pandas as pd
import matplotlib.pyplot as plt

def projection(dfLife: pd.DataFrame, gnp: pd.DataFrame):
    col_life = dfLife.loc[:, '1900']
    col_gnp = gnp.loc[:, '1900']
    
    print(col_life)
    print(col_gnp)
    plt.scatter(col_gnp, col_life)
    plt.xscale('log')
    # Set axis labels and title
    plt.xlabel('Gross Domestic Product (GDP)')
    plt.ylabel('Life Expectancy')
    plt.title('Life Expectancy vs GDP in 1900')
    # Set the x-ticks to correspond to the log scale
    plt.xticks([300, 1000, 3000, 10000], ['300', '1k', '3k', '10k'])
    plt.show()
    
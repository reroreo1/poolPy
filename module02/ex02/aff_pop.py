import pandas as pd
import matplotlib.pyplot as plt

def aff_pop(df: pd.DataFrame):
    df.set_index("country", inplace = True)
    df = df.loc[['Morocco','France']]
    def convert_population_to_float(pop_str):
        return float(pop_str.replace('M', '')) * 1e6
    # Apply the conversion to each cell in the DataFrame
    df = df.map(convert_population_to_float)
    # Transpose the DataFrame for plotting
    df_transposed = df.T
    # Plotting
    plt.figure(figsize=(12, 6))
    for country in df_transposed.columns:
        plt.plot(df_transposed.index, df_transposed[country] / 1e6, label=country)
    plt.title('Population Over Time')
    plt.xlabel('Year')
    plt.ylabel('Population (Millions)')
    years_to_show = [str(year) for year in range(1800, 2101, 40)]
    numbers_to_show = [20,40,60]
    plt.xticks(years_to_show, rotation=0)
    plt.yticks(numbers_to_show, rotation=0)
    plt.legend()
    plt.show()
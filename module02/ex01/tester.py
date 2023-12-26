from load_csv import load
from aff_life import aff_life


def main():
    path = "../life_expectancy_years.csv"
    aff_life(load(path))
    

if __name__ == "__main__":
    main()
from load_csv import load
from projection_life import projection


def main():
    path = "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    path1 = "../life_expectancy_years.csv"
    projection(load(path1),load(path))
    

if __name__ == "__main__":
    main()
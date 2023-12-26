from load_csv import load
from aff_pop import aff_pop


def main():
    path = "../population_total.csv"
    aff_pop(load(path))
    

if __name__ == "__main__":
    main()
# Itay Dvir
import pandas as pd


def main():

    # https://www.kaggle.com/datasets/justinas/nba-players-data?resource=download
    file_path = 'all_seasons.csv'

    df = pd.read_excel(file_path)
    desc = df.describe()
    print(desc)


if __name__ == '__main__':
    main()

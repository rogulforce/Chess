from data_get import data_get, create_csv
import pandas as pd
if __name__ == "__main__":

    a = data_get(r'E:\bigdata\lichess_db_standard_rated_2019-05.pgn', r'E:\bigdata\filtered_data_300600.csv',
                 break_point=500000000)
    # a = create_csv('s')
    # d = pd.read_csv(r'E:\bigdata\filtered_data.csv')
    #



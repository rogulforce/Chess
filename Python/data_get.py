import pandas as pd
from typing import List
import re


def line_filter(line: str) -> bool:
    # missed = ['[Site', '[Date', '[Roun', ]
    if line != '\n':
        return True
    return False


def results_to_table(data: list, df: pd.DataFrame):
    """ function filtering and cleaning data

    :param data: list of last 19 rows from file
    :param df: dataframe to save results
    :return: df
    """
    results = []
    if data[0][:6] == '[Event':
        for i in [0, 6, 9, 10, 11, 12, 13, 14, 15, 16]:
            results.append(re.search(r"\"(.*?)\"", data[i])[0][1:-1])
        results.append(data[-1])
        df = df.append(pd.DataFrame([results]), ignore_index=True)

    return df


def data_get(filename: str, to_filename: str, break_point: int = 50000000):
    """ function filtering data and saving it in csv format

    :param filename: .pgn file with saved games
    :param to_filename: .csv file to save results
    :return: None
    """
    with open(file=filename, mode='r', encoding='utf-8') as f:
        df = pd.DataFrame([])
        temp_data = []   # temporary held lines
        for i, line in enumerate(f):

            if i > break_point:
                break
            temp_data.append(line)
            if i % 10000 == 0:
                print(f'{100*i/break_point}%')
            if 'eval' in line:
                # print(temp_data[-19:])
                df = results_to_table(temp_data[-19:], df)
                temp_data.clear()
                # if line_filter(line) is True:
                # data.write(line)
    df = df.rename(columns={0: 'Event', 1: 'Result', 2: 'WhiteElo', 3: 'BlackElo', 4: 'WhiteRatingDiff',
                            5: 'BlackRatingDiff', 6: 'ECO', 7: 'Opening', 8: 'TimeControl', 9: 'Termination',
                            10: 'Game'})
    create_csv(df, to_filename)
    return


def create_csv(df: pd.DataFrame, to_file: str):
    """ funtion saving pandas table to .csv format

    :param df: dataframe
    :param to_file: file in csv format
    :return: None
    """
    df.to_csv(to_file, mode='w')
    return


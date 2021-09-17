import pandas as pd
from typing import List
import re


def line_filter(line: str) -> bool:
    # missed = ['[Site', '[Date', '[Roun', ]
    if line != '\n':
        return True
    return False


def results_to_table(data: list, df: pd.DataFrame, formats: list):
    """ function filtering and cleaning data

    :param data: list of last 19 rows from file
    :param df: dataframe to save results
    :param formats: list of formats to find in filename
    :return: df
    """

    if data[0][:6] == '[Event':
        if any(f in data[15] for f in formats):
            results = []
            for i in [6, 9, 10, 15]:
                results.append(re.search(r"\"(.*?)\"", data[i])[0][1:-1])
            results.append(data[-1])
            df = df.append(pd.DataFrame([results]), ignore_index=True)

    return df


def data_get(filename: str, to_filename: str, formats: list = ('300+0','600+0'), break_point: int = 5000000):
    """ function filtering data and saving it in csv format

    :param filename: .pgn file with saved games
    :param to_filename: .csv file to save results
    :param formats: list of formats to find in filename
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
                df = results_to_table(temp_data[-19:], df, formats)
                temp_data.clear()
                # if line_filter(line) is True:
                # data.write(line)
    df = df.rename(columns={0: 'Result', 1: 'WhiteElo', 2: 'BlackElo', 3: 'TimeControl',
                            4: 'Game'})
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


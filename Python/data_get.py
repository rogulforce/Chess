import pandas as pd


def line_filter(line):
    if line != '\n':
        return True
    return False


def data_get(filename):
    data = open('sample_out.txt', mode="w", encoding='utf-8')

    with open(file=filename, mode='r', encoding='utf-8') as f:

        for i, line in enumerate(f):
            if i<150:    # ile zapisanych linijek
                if line_filter(line) is True:
                    data.write(line)
    data.close()
    return


def line_filter(line):
    if line != '\n':
        return True
    return False


def data_get(filename):
    data = open('sample_out.txt', mode="w", encoding='utf-8')

    with open(file=filename, mode='r', encoding='utf-8') as f:
        for line in f:
            if line_filter(line) is True:
                data.write(line)
    data.close()
    return


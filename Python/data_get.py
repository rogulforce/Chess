def data_get(filename):
    with open(file=filename, mode='r', encoding='utf-8') as f:
        print(f.read())
    return


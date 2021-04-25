import numpy as np


def time_to_sec(hhmmss: str) -> int:
    """ function converting time to seconds

    :param hhmmss: str containing 'hh:mm:ss' format of time
    :return: number of seconds
    """
    return sum(x * int(t) for x, t in zip([3600, 60, 1], hhmmss.split(":")))


def diff(value_list: list, step: int = 1, reversed: bool = False) -> list:
    """function returning moving difference of each element in list based on previous values

    :param value_list: list containing  numeric values in order
    :param step: number of steps back to calculate difference, default: 1
    :param reversed: if values are descending, default: False
    :return: list of calculated differences
    """
    v_copy = [it for it in value_list]
    for i in range(len(v_copy)-1, -1, -1):
        if i in np.arange(step):
            v_copy[i] = 0
        if i >= step:
            v_copy[i] = v_copy[i] - v_copy[i-step]
    if reversed:
        v_copy = [-1 * it for it in v_copy]
    return v_copy

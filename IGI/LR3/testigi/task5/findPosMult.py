def findPosMult(lst: list):
    """Find multiplication of positive elements"""
    res: float = 1
    for el in lst:
        if el > 0:
            res *= el
    return res
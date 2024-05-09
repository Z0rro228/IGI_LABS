def findCustomSum(lst: list) -> float:
    """Find sum of elements that staying before the element with min abs."""
    res: float = 0
    minAbs: float = abs(lst[0])
    for el in lst:
        if abs(el) < minAbs:
            minAbs = abs(el)
    for el in lst:
        if abs(el) == minAbs:
            break
        res += el
    return res
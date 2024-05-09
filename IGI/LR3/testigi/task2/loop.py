def loop() -> int:
    """Calcultate number of elements greater than 12 in the sequence."""
    stringNums = input()
    counter: int = 0
    parts = stringNums.split(' ')
    for p in parts:
        a: int
        try:
            a = int(p)
            if(a > 12):
                counter+=1
            elif a == 0:
                break
        except:
            print(f"Wrong format!!! {p}")
            break

    return counter
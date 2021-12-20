def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    x = list(d.keys())
    x1 = []
    if isinstance(x[0], int):
        return (min(x), max(x))
    elif isinstance(x[0], str):
        for word in x:
            x1.append(len(word))
        return (x[x1.index(min(x1))], x[x1.index(max(x1))])
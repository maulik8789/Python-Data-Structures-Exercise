def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    check = 0
    for item in lst:
        if isinstance(item, list):
            check += 1
    if check == len(lst):
        return True
    else:
        return False


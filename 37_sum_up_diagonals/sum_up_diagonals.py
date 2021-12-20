def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    sum1 = 0
    sum2 = 0

    x = range(0, len(matrix))
    for i in x:
        sum1 = sum1 + matrix[i][i]

    x = range(len(matrix) - 1, -1, -1)
    for i in x:
        sum2 = sum2 + matrix[len(matrix) -1 - i][i]
    
    return sum1 + sum2

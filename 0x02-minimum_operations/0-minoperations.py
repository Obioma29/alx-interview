#!/usr/bin/python3
""" Minimum operations
    """

def minOperations(n: int) -> int:
    """ Method to compute the minimum number of operations """

    z = 'H'
    i  = 'H'
    op = 0
    while (len(i) < n):
        if n % len(i) == 0:
            op += 2
            z = i
            i += i
        else:
            op += 1
            i += z
    if len(i) != n:
        return 0
    return op

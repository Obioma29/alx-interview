#!/usr/bin/python3
""" Minimum Operations
    """

def minOperations(n: int) -> int:
    """ Minimum Operations needed 
        to get n H characters """

    z = 'H'
    i = 'H'
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

#!/usr/bin/python3
""" A Script that shows the  minimum operations needed 
in a CopyAll - Paste operation """

def minOperations(n: int) -> int:
    """ Method for compute the minimum number of 
    operations for task Copy All and Paste """

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

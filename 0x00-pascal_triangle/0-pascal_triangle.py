#!/usr/bin/python3
"""
Pascal's Trangle
"""


def pascal_triangle(n):
    '''
    Creates a list of lists of integers in a Pascal's triangle
    for a given integer.
    '''
    if n <= 0:
        return []
    else:
        result = []
        for i in range(n):
            if len(result) == 0:
                result.append([1])
            else:
                row = [1]
                for j in range(1, len(result[-1])):
                    row.append(result[-1][j] + result[-1][j - 1])
                row.append(1)
                result.append(row)
        return result

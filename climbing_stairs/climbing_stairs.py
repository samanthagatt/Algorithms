#!/usr/bin/python

import sys

"""
# least steps (didn't read the instructions correctly)
def climbing_stairs(n, cache=None):
    threes = int(n / 3)
    left_over = n % 3
    twos = int(left_over / 2)
    ones = left_over % 2
    return threes + twos + ones
"""


def climbing_stairs(n, cache={}):
    """
    if n == 0:
        return 1
    elif n == 1 or n == 2:
        return n
    else:
        return climbing_stairs(n-1) + climbing_stairs(n-2)
        + climbing_stairs(n-3)
    """
    # memoization
    """
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    elif n in cache:
        return cache[n]
    else:
        cache[n] = climbing_stairs(n-1, cache) + climbing_stairs(n-2, cache)
        + climbing_stairs(n-3, cache)
        return cache[n]
    """

    if n == 0:
        return 1
    if n <= 2:
        return n

    prev_prev_prev = 1
    prev_prev = 1
    prev = 2
    cur = 0

    for _ in range(2, n):
        cur = prev + prev_prev + prev_prev_prev
        prev_prev_prev = prev_prev
        prev_prev = prev
        prev = cur

    return cur


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs
        ))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')

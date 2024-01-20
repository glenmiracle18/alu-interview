#!/usr/bin/python3
""" minimum operator function """


def minOperations(n):
    """
    calculates minimum operations to copy and test text
    """
    if n == 1:
        return 0  # base case: already have h in the file

    operations = 0
    divisor = 2  # start with the smallest prime divisor

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations

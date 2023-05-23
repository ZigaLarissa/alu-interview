#!/usr/bin/python3
import math


def minOperations(n):
    if n == 0:
        return 0
    
    operations = 0
    
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            operations += i 
            n = n // i

    if n > 1:
        operations += n
    
    return operations
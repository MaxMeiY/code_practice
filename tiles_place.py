'''
page78
Given an empty plot of size 2*n. we want to place tiles
such that the entire plot is coverd. Each tile is of size
2*1 and can be placed either horizontally or vertically.
see page78<Dynamic Programming for Coding Interviews>
'''

def solution(n):
    if n == 0 or n == 1:
        return 1
    return solution(n-1) + solution(n-2)

def f(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    return f(n-2) + 2 * g(n-1)

def g(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    return f(n-1) + g(n-2)
'''
page47

Given a matrix of N*N.
what're the total number of ways in which we can move form
top-left (array[0][0]) to the bottom-right(array[n-1][n-1]), given that we can only move either downward or rightward
'''

def count(array, row, col):
    # if either 0, there's only one way
    if row == 1 or col == 1:
        return 1
    
    maximum = count(array, row-1, col) + \
              count(array, row, col-1)

    return maximum

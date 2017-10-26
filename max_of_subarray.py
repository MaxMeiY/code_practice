'''
page 82
Given an array of integers, write a function that returns
the maximum sum of sub array, such that elements are
contiguous.
'''

def solution(array):
    '''
    Input:[-2,-3,4,-1,-2,1,5,-3]
    Output: 7
    (4, -1, -2, 1, 5)
    '''
    n = len(array)
    max_sum = 0

    for i in range(n):
        temp = array[i]
        for j in range(i+1,n):
            temp = temp + array[j]
            if temp > max_sum:
                max_sum = temp
    return max_sum

def kadane_algorithm(array):
    max_sum = array[0]
    max_ending_here = array[0]
    n = len(array)

    for i in range(1, n):
        max_ending_here = max(array[i],
                              max_ending_here + array[i])
        max_sum = max(max_sum, max_ending_here)

    return max_sum
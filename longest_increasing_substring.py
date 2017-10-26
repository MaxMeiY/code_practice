'''
page115
Given an array of integers, write code that returns length
of longest monotonically increasing subsequence in the array.
'''

def solution(array):
    memo = [1] * len(array)
    max_length = 0

    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            memo[i] = memo[i-1] + 1
            if memo[i] > max_length:
                max_length = memo[i]
        else:
            memo[i] = 1

    print(memo)

    return max_length

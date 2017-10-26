'''
page103
Given an array of non-negative integers and a positive
number x, determine if there exist a subset of the elements of array with sum equal to x.
'''

def solution(array,x):
    '''
    Input: (3,2,7,1) x = 6
    Output: true   cause(3,2,1) == 6
    '''
    if x == 0:
        return True
    if len(array) == 0:
        return False
    return solution(array[1:], x-array[0]) or \
           solution(array[1:], x)


def DP_solution(array, x):
    memo = [[None for _ in range(len(array))] for _ in range(x+1)]

    for i in range(len(array)):
        memo[0][i] = True

    for j in range(1, x+1):
        if array[0] == j:
            memo[j][0] = True
        else:
            memo[j][0] = False

    for i in range(1, x+1):
        for j in range(1, len(array)):
            if i >= array[j]:
                memo[i][j] = memo[i][j-1] or \
                             memo[i-array[j]][j]
            else:
                memo[i][j] = memo[i][j-1]
    return memo[x][len(array)-1]


if __name__ == '__main__':
    a = [3,2,7,1]
    print(solution(a,-10))
    print(DP_solution(a,6))
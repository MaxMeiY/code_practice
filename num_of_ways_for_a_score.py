'''
page80
Given score 3, 5, 10 in one move, and a total score N.
find the total number of unique ways to reach a score of
N
'''

def solution(n):
    '''
    Input: n=13
    Output: 5
    '''
    if n < 0:
        return 0
    elif n == 0:
        return 1
    return solution(n-3) + solution(n-5) + solution(n-10)

def DP_solution(n):
    '''
    (10,3) (3,10) are considered same.
    Modified version
    '''
    memo = [0] * (n+1)
    memo[0] = 1

    for i in range(1, n+1):
        if i - 3 >= 0:
            if i - 3 != 5 and i -3 != 10:
                memo[i] += memo[i-3]
        if i  - 5 >= 0:
            if i - 5 != 10:
                memo[i] += memo[i-5]

        if i - 10 >= 0:
            memo[i] += memo[i-10]
    print(memo)

    return memo[n]

        

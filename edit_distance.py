'''
page 85
Given two strings str1 and str2 and three methods
1.Insert
2.Remove
3.Replace
Find minimum of operations to convert str1 to str2
'''

def solution(str1, str2):
    # Insert len(str2)
    if len(str1) == 0:
        return len(str2)
    # Remove str1
    if len(str2) == 0:
        return len(str1)
    # if the same
    if str1[0] == str2[0]:
        return solution(str1[1:], str2[1:])

    # delete one
    d = solution(str1[1:], str2)
    # replace one
    u = solution(str1[1:], str2[1:])
    # insert one
    i = solution(str1,str2[1:])

    return min(d,u,i) + 1

def DP_solution(str1, str2):
    n = len(str1)
    m = len(str2)

    memo = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(m+1):
        memo[0][i] = i

    for i in range(n+1):
        memo[i][0] = i

    for i in range(1,n+1):
        for j in range(1,m+1):
            if str1[i-1] == str2[j-1]:
                memo[i][j] = memo[i-1][j-1]
            else:
                memo[i][j] = min(memo[i-1][j-1],
                                 memo[i][j-1],
                                 memo[i-1][j]) + 1
    return memo[n][m]
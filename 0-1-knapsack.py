'''
page 126
0-1 knapsack
'''

def solution(W, V, c,n):
    if n <= 0 or c <= 0:
        return 0
    if W[n-1] > c:
        return solution(W, V, c, n-1)
    return max(solution(W, V, c-W[n-1], n-1)+V[n-1],
               solution(W, V, c, n-1))


def DP_solution(W,V, c, n):
    memo = [[0 for _ in range(c+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, c+1):
            if j >= W[i-1]:
                x = j - W[i-1]
                memo[i][j] = max(memo[i-1][j],
                                 V[i-1] + memo[i-1][x])
            else:
                memo[i][j] = memo[i-1][j]

    print(memo)
    return memo[n][c]





if __name__ == '__main__':
    w = [2,3,4,5]
    v = [3,4,5,6]
    print(solution(w,v,5,4))
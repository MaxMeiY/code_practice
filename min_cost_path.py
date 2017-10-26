'''
page69
Given a two-dim square matrx cost[][] of order M*N where
cost[i][j] represents the cost of passing though cell(i,j)
Total cost to reach a particular cell is the sum of costs
of all the cells in that path.
We can only move either downward or rightward.
i.e. if at cell (i, j), we can either go to cell (i, j+1)
or to (i+1, j)
'''

def solution(cost, m, n):
    if m == 0 and n == 0:
        return cost[0][0]
    elif m == 0:  # first row
        return solution(cost, 0, n-1) + cost[0][n]
    elif n == 0:  # left col
        return solution(cost, m-1, 0) + cost[m][0]
    else:
        x = solution(cost, m-1, n)
        y = solution(cost, m, n-1)
        return min(x, y) + cost[m][n]

def DP_solution(cost, m, n):
    memo = [[0 for _ in range(n)] for _ in range(m)]
    memo[0][0] = cost[0][0]

    # init memo
    for i in range(1,n):
        memo[0][i] = cost[0][i] + memo[0][i-1]
    for j in range(1,m):
        memo[j][0] = cost[j][0] + memo[j-1][0]
    print(memo)

    for i in range(1,m):
        for j in range(1,n):
            minimum = min(memo[i-1][j], memo[i][j-1])
            memo[i][j] = cost[i][j] + minimum

    return memo[m-1][n-1]





if __name__ == '__main__':
    cost = [[1,3,5,8], [4,2,1,7],[4,3,2,3]]
    print(solution(cost, 2,3))
    print(DP_solution(cost,3,4))
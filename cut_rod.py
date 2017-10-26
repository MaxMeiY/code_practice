'''
page 121
Cutting a rod
'''

def solution(values, n):
    '''
    Nothing needs to be said
    '''
    if n <= 0:
        return 0

    max_value = float("-inf")

    for i in range(1,n+1):
        max_value = max(max_value,
                        values[i] + solution(values, n-i))

    return max_value

def DP_solution(values, n):
    memo = [0] * (n + 1)

    for i in range(1,n+1):
        for j in range(i):
            memo[i] = max(memo[i],
                          values[j] + memo[i-j-1])

    print(memo)
    return memo[n]




if __name__ == '__main__':
    values = [1,5,8,9,10,17,17,20]
    print(solution(values, 4))
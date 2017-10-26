'''
page 116
Coin Change
'''

def solution(coins, s):
    if s == 0:
        return 0
    minimum = float("inf")

    for i in range(len(coins)):
        if s >= coins[i]:
            temp = solution(coins,s-coins[i])

            if temp + 1 < minimum:
                minimum = temp + 1
    return minimum

def variant_coin_change(coins, s):
    if s == 0:
        return 1
    if s < 0 or len(coins) <= 0:
        return 0
    return variant_coin_change(coins[1:], s) + \
        variant_coin_change(coins, s-coins[0])

def DP_solution(coins, s):
    memo = [float("inf")] * (s+1)

    memo[0] = 0

    # from 1 to s
    for i in range(1,s+1):
        # try every coin
        for j in range(len(coins)):
            if i >= coins[j]:
                temp = memo[i-coins[j]]

                if temp != float("inf") and \
                   temp + 1 < memo[i]:
                    memo[i] = temp + 1
    return memo[s]
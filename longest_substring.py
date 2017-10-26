'''
page58
'''

def solution(string):
    '''
    Find length of longest substring of a given string of
    digits, such that sum of digits in the first half and
    second half of the substring is same.
    Input: '142124'
    Output: 6
    (1+4+2 = 1+2+4)

    Input: '9430723'
    Output: 4
    (4 + 3 = 0 + 7)
    '''
    l = len(string)
    max_length = 0

    # start index
    for i in range(l):
        # end index
        for j in range(i+1, l, 2):
            length = j - i + 1

            if max_length >= length:
                continue

            lsum, rsum = 0, 0
            for k in range(0, length//2):
                lsum += int(string[i+k])
                rsum += int(string[i+k+length//2])

            if lsum == rsum:
                max_length = length
    return max_length

def DP_longest_substring(string):
    l = len(string)

    if l <= 0:
        return
    memo = [[0 for _ in range(l)] for _ in range(l)]

    for i in range(l):
        memo[i][i] = int(string[i])

    max_length = 0
    for length in range(2, l+1):
        # pick up i, j
        for i in range(0, l-length+1):
            j = i + length - 1
            k = length // 2

            memo[i][j] = memo[i][j-k] + memo[j-k+1][j]

            if length % 2 == 0 and memo[i][j-k] == memo[j-k+1][j] and length > max_length:
                max_length = length
    return max_length

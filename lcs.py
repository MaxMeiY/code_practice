'''
longest common substring
wrote it myself
'''

def lcs(string1, string2):
    n = len(string1)
    m = len(string2)

    memo = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if string1[j-1] == string2[i-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j],
                                 memo[i][j-1])

    return memo[m][n],memo

def print_lcs(str1,str2,m,n):
    length,memo = lcs(str1,str2)

    result = []

    while length > 0:
        if str1[m-1] == str2[n-1]:
            result.append(str1[m-1])
            m -= 1
            n -= 1
            length -= 1
        elif memo[n-1][m] > memo[n][m-1]:
            n -= 1
        else:
            m -= 1
    return result



if __name__ == '__main__':
    s1 = 'abcd'
    s2 = 'aebd'
    print(lcs(s1,s2))

    print(print_lcs(s1,s2,len(s1),len(s2)))
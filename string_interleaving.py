'''
page96
String C is said to be interleaving of string A and B if
it contains all the characters of A and B and the relative
order of characters of both the strings is preserved in C
'''

def WRONG_VERSION_solution(A, B, C):
    '''
    SEE THE PRINT VALUE
    Input: A = 'xyz' B = 'abcd'
    Output: C = xabyczd
    '''

    if len(C) != len(A) + len(B):
        return False
    i = 0
    j = 0
    k = 0
    for i in range(len(C)):
        print(C[i])
        print(i,j,k)
        if C[i] != A[j] and C[i] != B[k]:
            return False
        elif C[i] == A[j]:
            j += 1
        elif C[i] == B[k]:
            k += 1
        else:
            return False
    return True

def solution(A, B, C):
    if len(A) == len(B) == len(C) == 0:
        return True
    if len(C) == 0:
        return False
    if len(A) == 0 and len(B) == 0:
        return False
    first = False
    second = False

    if A and A[0] == C[0]:
        first = solution(A[1:],B, C[1:])
    if B and B[0] == C[0]:
        second = solution(A, B[1:], C[1:])

    return first or second

def DP_solution(A,B,C):
    memo = [[None for _ in range(len(B)+1)] for _ in range(len(A)+1)]
    memo[0][0] = True

    for i in range(1, len(A)+1):
        if C[i-1] == A[i-1]:
            memo[i][0] = memo[i-1][0]
        else:
            memo[i][0] = False

    for j in range(1, len(B)+1):
        if C[j-1] == B[j-1]:
            memo[0][j] = memo[0][j-1]
        else:
            memo[0][j] = False

    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if C[i+j-1] != A[i-1] and \
               C[i+j-1] != B[j-1]:
                memo[i][j] = False
            elif C[i+j-1] == A[i-1] and \
                 C[i+j-1] == B[j-1]:
                memo[i][j] = memo[i-1][j] or memo[i][j-1]
            elif C[i+j-1] == A[i-1]:
                memo[i][j] = memo[i-1][j]
            else:
                memo[i][j] = memo[i][j-1]

    print(memo)
    return memo[len(A)][len(B)]
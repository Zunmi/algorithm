def ord_c(c):
        return ord(c) - ord('a')
def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    m,n,k = len(T), len(S), len(S[0])
    A = [0]*n
    Frequency = [0]*26
    Hash = {}
    for i in range(m):
        Frequency[ord_c(T[i])] +=1
        if i > k-1:
            Frequency[ord_c(T[i-k])] -=1
        if i >= k-1:
            key = tuple(Frequency)
            if key in Hash:
                Hash[key] += 1
            else:
                Hash[key] = 1

    for i in range(n):
        F = [0]*26
        for c in S[i]:
            F[ord_c(c)] += 1
        key = tuple(F)
        if key in Hash:
            A[i] = Hash[key]

    return tuple(A)

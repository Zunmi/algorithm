def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 1
    n = len(A)
    current_length = 1
    length = 1
    for i in range(1, n):
        if A[i] > A[i - 1]:
            current_length += 1
        else:
            current_length = 1
        if current_length > length:
            length = current_length
            count = 1
        elif current_length == length:
            count += 1
    return count

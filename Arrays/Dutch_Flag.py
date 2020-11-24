
def dutch_flag(A):
    low, mid, high = 0, 0, len(A)
    while mid < high:
        if A[mid] == 'R':
            A[low], A[mid] = A[mid], A[low]
            low, mid = low + 1, mid + 1
        elif A[mid] == 'G':
            mid += 1
        else:
            high -= 1
            A[mid], A[high] = A[high], A[mid]
    return A


A = ['G','R','R','B','G','R','B']
print(dutch_flag(A))

def dutch_flag_four_colors(A):
    left = A[0]
    mid_left, right, left_i, mid_left_i = None, None, 0, 0
    mid_right_i, right_i = len(A), len(A)

    while mid_left_i < right_i and mid_left_i< mid_right_i:
        if (A[mid_left_i] == left):
            A[mid_left_i], A[left_i] = A[left_i], A[mid_left_i]
            mid_left_i += 1
            left_i += 1
        elif right is None or A[mid_left_i] == right:
            right_i -= 1
            mid_right_i = right_i
            A[mid_left_i], A[right_i] = A[right_i], A[mid_left_i]
            right = A[right_i]
        else:
            if mid_left is None:
                mid_left = A[mid_left_i]
            if A[mid_left_i] == mid_left:
                mid_left_i += 1
            else:
                mid_right_i -= 1
                A[mid_left_i], A[mid_right_i] = A[mid_right_i], A[mid_left_i]
    return A

print(dutch_flag_four_colors([1,2,1,2,3,1,4,1]))

def Solution (l : list[int]):

    # Logic:
    # mat[0][i] contains the longest increasing sub-interval ending at i (meaning its last value is at index i)
    # mat[1][i] contains the longest increasing sub-interval up to i
    # Formula for determining values
    # mat[0][i] = mat[0][i - 1] + 1 if list[i] > list[i - 1]
    #           = 1 if list[i] <= list[i - 1]
    # mat[1][i] = max(mat[1][i - 1], mat[0][i])

    # Things to Consider:
    # Length >= 1

    mat = [[-1 for i in range(len(l))] for j in range(2)]
    mat[0][0] = 1
    mat[1][0] = 1

    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            mat[0][i] = mat[0][i - 1] + 1
        else:
            mat[0][i] = 1
        mat[1][i] = max(mat[1][i - 1], mat[0][i])
    return mat[1][-1]

test = [2, 5, 1, 3, 4, 5, 5, 1] # 4: 1, 3, 4, 5
print(Solution(test))


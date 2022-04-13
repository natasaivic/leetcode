# 1572. Matrix Diagonal Sum

# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal 
# and all the elements on the secondary diagonal that are not part of the primary diagonal.


def diagonalSum(mat):
    n = len(mat)
    mid = n // 2
    total = 0

    for i in range(n):
        total += mat[i][i] 
        total += mat[i][n-1-i]

    # when n is Odd
    if n // 2 == 1:
        total -= mat[mid][mid]

    return total
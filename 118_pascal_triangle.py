# 118. Pascal's Triangle

# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


def pascalTriangle(numRows):
    pascal = [[1]*(i + 1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

    return pascal

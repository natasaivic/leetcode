# 200. Number of Islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
# return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.


class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = '0'
        adjacent_land = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for row, col in adjacent_land:
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[row]) and grid[row][col] == '1':
                self.dfs(grid, row, col)

    def numIslands(self, grid):
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    islands += 1

        return islands

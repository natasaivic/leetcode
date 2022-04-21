# 695. Max Area of Island

# You are given an m x n binary matrix grid. 
# An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
# You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.


class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        num = 1
        adjacent_islands = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for row, col in adjacent_islands:
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[row]) and grid[row][col] == 1:
                num += self.dfs(grid, row, col)
                
        return num
    
    def maxAreaOfIsland(self, grid):
        area_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    area_islands = max(area_islands, self.dfs(grid, r, c))
                    
        return area_islands
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        x = len(grid[0])-1
        y = len(grid)-1
        for i in range(x-1, -1, -1):
            grid[-1][i] += grid[-1][i+1]
        for i in range(y-1, -1, -1):
            grid[i][-1] += grid[i+1][-1]
        for i in range(y-1, -1, -1):
            for j in range(x-1, -1, -1):
                grid[i][j] += min(grid[i+1][j], grid[i][j+1])
        return grid[0][0]
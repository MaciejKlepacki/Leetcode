class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        x = len(obstacleGrid[0])
        y = len(obstacleGrid)
        grid = [[0 for _ in range(x)] for _ in range(y)]

        #
        i, stone = x - 1, False
        while i != -1 and stone != True:
            if obstacleGrid[y - 1][i] == 1:
                stone = True
            else:
                grid[y - 1][i] = 1
                i -= 1

        #
        i, stone = y - 1, False
        while i != -1 and stone != True:
            if obstacleGrid[i][x - 1] == 1:
                stone = True
            else:
                grid[i][x - 1] = 1
                i -= 1


        for i in range(x-2, -1, -1):
            for j in range(y-2, -1, -1):
                if obstacleGrid[j][i]==0:
                    grid[j][i] = grid[j+1][i] + grid[j][i+1]

        return grid[0][0]
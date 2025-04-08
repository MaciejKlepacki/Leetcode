class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for level in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[level])):
                triangle[level][i] += min(triangle[level + 1][i], triangle[level + 1][i + 1])
        return triangle[0][0]
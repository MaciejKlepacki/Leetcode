class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows = rowIndex+1
        arr = [None] * numRows
        for i in range(numRows):
            arr[i] = [1] * (i + 1)
            if i > 1:
                for j in range(1, i):
                    arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
        return arr[rowIndex]
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ['' for _ in range(numRows)]
        numRows -= 1
        cur_row = 0
        adding = True
        for char in s:
            rows[cur_row] += char
            if adding and numRows > cur_row: cur_row += 1
            elif adding and numRows == cur_row:
                cur_row -= 1
                adding = False
            elif not adding and cur_row > 0: cur_row -= 1
            elif not adding and cur_row == 0:
                cur_row += 1
                adding = True
        result = ''
        for i in rows:
            result += i
        return result
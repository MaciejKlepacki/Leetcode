class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in range(1, len(columnTitle)+1):
            char_val = ord(columnTitle[-i]) - 64
            result += char_val*(26**(i-1))
        return result
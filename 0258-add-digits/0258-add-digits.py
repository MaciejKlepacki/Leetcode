class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9: return num
        while num > 9:
            result = 0
            for i in str(num):
                result += int(i)
            num = result
        return num
class Solution:
    def totalMoney(self, n: int) -> int:
        result = 0
        i = 0
        while n >= 7:
            result += (i*7) + 28
            n -= 7
            i += 1

        for j in range(1,n+1):
            result += i + j
        return result
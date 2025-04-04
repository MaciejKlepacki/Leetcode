class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x*=-1
        x = str(x)[::-1]
        x = int(x)*sign

        if x > 2**31-1 or x < -2**31: return 0
        return x
# O(N)
class Solution:
    def myAtoi(self, s: str) -> int:
        if s == '': return 0
        while s[0]==' ' and len(s)!=1:
            s = s[1:]
        if s == '' or s == ' ': return 0
        result = 0
        sign = 1
        if s[0]=='-':
            sign = -1
            s = s[1:]
        elif s[0]=='+':
            s = s[1:]

        for char in s:
            if '0' <= char <= '9': result = result*10 + int(char)
            else: break

        result *= sign

        MIN = -2**31
        MAX = 2**31 - 1
        if result < MIN: return MIN
        elif result > MAX: return MAX

        return result
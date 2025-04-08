class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=0
        result = 0
        s = s[::-1] + ' '
        while s[i]==' ': i+=1
        while s[i]!=' ' and s[i+1]:
            i+=1
            result += 1
        return result
class Solution:
    def firstUniqChar(self, s: str) -> int:
        T = [0]*26
        for char in s:
            T[ord(char)-97] += 1
        for i in range(len(s)):
            if T[ord(s[i])-97] == 1: return i
        return -1
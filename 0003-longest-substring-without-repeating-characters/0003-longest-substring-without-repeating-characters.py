class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 1: return 1
        l, r = 0, 0
        max = 0
        while r < n and l < n:
            cur = s[l:r+1]
            if len(set(cur)) == len(cur) and r < n:
                r += 1
                if len(cur) > max: max = len(cur)
            else:
                l += 1
        return max
        
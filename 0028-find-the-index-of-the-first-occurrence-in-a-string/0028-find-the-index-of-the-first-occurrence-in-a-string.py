class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for l in range(len(haystack) - len(needle) + 1):
            r = l + len(needle)
            if haystack[l:r] == needle: return l
        return -1
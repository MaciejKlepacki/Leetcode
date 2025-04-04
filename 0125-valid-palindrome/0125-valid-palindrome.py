class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        string = ''
        for i in s:
            if i.isalpha() or i.isdigit(): string += i
        return string[::-1] == string
        
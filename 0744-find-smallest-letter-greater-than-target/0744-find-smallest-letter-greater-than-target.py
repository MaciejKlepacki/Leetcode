class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0] or target >= letters[-1]: return letters[0]
        for i in range(len(letters)-1):
            if letters[i] < target < letters[i+1]: return letters[i+1]
            elif letters[i] == target:
                i += 1
                while letters[i] == target: i += 1
                return letters[i]
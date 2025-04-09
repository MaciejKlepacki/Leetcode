class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negative = positive = 0
        for i in nums:
            if i > 0: positive += 1
            elif i < 0: negative += 1
        return max(positive, negative)
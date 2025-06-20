class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j] and dp[i]<dp[j]+1:
                    dp[i] = dp[j] + 1
        return max(dp)
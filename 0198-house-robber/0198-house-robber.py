class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        F = [0]*n
        F[0]=nums[0]
        F[1] = max(nums[0], nums[1])

        for i in range(2, n):
            F[i] = max(F[i-1], F[i-2]+nums[i])

        return F[n-1]
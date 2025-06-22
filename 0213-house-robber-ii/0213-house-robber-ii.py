class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        elif n==2:
            return max(nums[0], nums[1])
        dp1 = [0 for _ in range(n)]
        dp2 = [0 for _ in range(n)]
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        dp2[1] = nums[1]

        for i in range(1, n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])
        dp1[n-1] = dp1[n-2]
        dp2[n-1] = max(dp2[n-2], dp2[n-3] + nums[n-1])

        return max(dp1[n-1], dp2[n-1])
        
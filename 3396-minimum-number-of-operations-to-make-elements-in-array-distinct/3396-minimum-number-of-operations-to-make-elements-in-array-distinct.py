class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        i = 0
        while len(set(nums)) != len(nums) and len(nums) >= 3:
            nums = nums[3::]
            i += 1
        if len(set(nums)) != len(nums): i += 1
        return i
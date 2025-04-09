class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for i in nums:
            if k > i: return -1
        x = set(nums)
        return len(x.discard(k)) if x.discard(k)!=None else len(x)
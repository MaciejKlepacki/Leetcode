class Solution(object):
    def majorityElement(self, nums):
        best = nums[0]
        counter = 0
        for i in nums:
            if i == best: counter += 1
            else:
                if counter == 1: 
                    best = i
                else: counter -= 1
        return best
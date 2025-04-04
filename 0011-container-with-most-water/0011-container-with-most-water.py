class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max = 0
        while left != right:
            area = min(height[left], height[right]) * (right - left)
            if area > max: max = area
            if height[left] >= height[right]:
                right -= 1
            else: left += 1
        return max
        
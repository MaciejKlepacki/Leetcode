class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        # Prealokujemy listę o ustalonym rozmiarze
        result = [None] * (len(left) + len(right))
        l = r = index = 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result[index] = left[l]
                l += 1
            else:
                result[index] = right[r]
                r += 1
            index += 1
        # Przepisujemy pozostałe elementy lewej tablicy
        while l < len(left):
            result[index] = left[l]
            l += 1
            index += 1
        # Przepisujemy pozostałe elementy prawej tablicy
        while r < len(right):
            result[index] = right[r]
            r += 1
            index += 1
        return result
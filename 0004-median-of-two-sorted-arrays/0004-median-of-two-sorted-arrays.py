class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        T = [0 for _ in range(n+m)]
        l, r = 0, 0
        while l < n and r < m:
            if nums1[l] <= nums2[r]:
                T[l+r] = nums1[l]
                l += 1
            else:
                T[l+r] = nums2[r]
                r += 1
        while l < n:
            T[l+r] = nums1[l]
            l += 1
        while r < m:
            T[l+r] = nums2[r]
            r += 1
        if len(T)%2 == 0:
            middle1 = len(T)//2
            middle2 = len(T)//2 - 1
            return (T[middle1] + T[middle2]) / 2
        else:
            return T[(len(T) // 2)]
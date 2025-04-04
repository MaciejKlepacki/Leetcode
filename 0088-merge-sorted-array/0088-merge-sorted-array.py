class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        arr = [0]*(m+n)
        cur1 = cur2 = 0
        while cur1<m and cur2<n:
            if nums1[cur1] <= nums2[cur2]:
                arr[cur1+cur2] = nums1[cur1]
                cur1+=1
            else:
                arr[cur1+cur2] = nums2[cur2]
                cur2+=1
        while cur1<m and cur2==n:
            arr[cur1+cur2] = nums1[cur1]
            cur1+=1
        while cur2<n:
            arr[cur1+cur2] = nums2[cur2]
            cur2+=1
        for i in range(len(arr)):
            nums1[i] = arr[i]
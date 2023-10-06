class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            ini = m + i
            while ini > 0 and nums1[ini-1] > nums2[i]:
                nums1[ini] = nums1[ini-1]
                ini -= 1
                print(nums1)
            nums1[ini] = nums2[i]
    
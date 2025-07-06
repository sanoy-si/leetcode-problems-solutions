class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.counter[self.nums2[index]] -= 1
        self.counter[val + self.nums2[index]] += 1 
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        count = 0
        for num in self.nums1:
            count += self.counter[tot - num]
        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
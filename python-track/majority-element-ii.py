class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return list(filter(lambda x: counter[x] > len(nums)/3, list(counter.keys())))
        
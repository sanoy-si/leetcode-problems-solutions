class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted((nums))
        d = {}
        for i,num in enumerate(sorted_nums):
            if num not in d:
                d[num] = i

        answer = [d[num] for num in nums]

        return answer        
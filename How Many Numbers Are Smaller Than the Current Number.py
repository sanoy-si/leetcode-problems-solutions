def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s=list(sorted(nums))
        l=[]
        for i in nums:l.append(s.index(i))
        return l

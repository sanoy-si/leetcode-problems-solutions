 def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums=list(sorted(nums))
        try:
            vs=[]
            vs.append(nums.index(target))
        except:return []
        for i in range(nums.count(target)-1):
            vs.append(vs[-1]+1)
        return vs

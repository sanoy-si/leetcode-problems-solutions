class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        nums=list(sorted(list(c.items()),key=lambda x:x[1],reverse=True))
        ans=[]
        print(nums)
        for i in range(k):
            ans.append(nums[i][0])
        return ans 

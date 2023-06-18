class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        lq=len(l)
        ln=len(nums)
        answer=[]
        for i in range(lq):
            answer.append(self.can(nums[l[i]:r[i]+1]))
        return answer
    def can(self,arr):
        arr.sort()
        ln=len(arr)
        if ln<2:return False
        d=arr[1]-arr[0]
        for i in range(2,ln):
            if arr[i]-arr[i-1]!=d:return False
        return True

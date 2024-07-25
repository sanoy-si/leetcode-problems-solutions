from math import floor
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        return self.divide(nums,0,len(nums)-1)
    def divide(self,nums,s,e):
        if e-s+1<=1:
            return nums[s:e+1]
        m=floor((e+s)/2)
        ll=self.divide(nums,s,m)
        rl=self.divide(nums,m+1,e)
        return self.merge(ll,rl)
    
    def merge(self,ll,rl):
        temp=[]
        lc=0
        rc=0
        lln=len(ll)
        rln=len(rl)
        while lc<lln and rc<rln:
            if ll[lc]<=rl[rc]:
                temp.append(ll[lc])
                lc+=1
            else:
                temp.append(rl[rc])
                rc+=1
        if lc<lln:
            temp.extend(ll[lc:])
        elif rc<rln:temp.extend(rl[rc:])
        return temp

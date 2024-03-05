class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        tempList=[]
        result=[]
        def backtracking(index,target):
            if target==0:
                result.append(tempList.copy())
                return
            if index>=len(candidates) or target<0:
                return
            for i in range(index,len(candidates)):
                if(target-candidates[i]>=0):
                    tempList.append(candidates[i])
                    ## add the same number or 
                    backtracking(i,target-candidates[i])
                    tempList.pop()
                # add a different number
            # backtracking(i+1,target)
            
        backtracking(0,target)
        return result
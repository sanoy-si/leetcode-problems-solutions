class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ln=len(arr)
        ans=[]
        right=ln-1
        while right:
            if arr[right]==right+1:right-=1
            else:
                ans.append(arr.index(right+1)+1)
                arr=list(reversed(arr[0:ans[-1]]))+arr[ans[-1]:]
                ans.append(right+1)
                arr=list(reversed(arr[0:ans[-1]]))+arr[ans[-1]:]

                
        return ans

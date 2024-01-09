class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        reverse = False
        for i in range(1,len(arr)):
            if not reverse:
                if arr[i] <= arr[i-1]:
                    if i == 1:
                        return False
                    reverse = True
            
            if reverse:
                if arr[i] >= arr[i-1]:
                    return False
        
        if not reverse:
            return False
        
        return True
                

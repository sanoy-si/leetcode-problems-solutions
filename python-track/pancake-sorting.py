class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ks = []
        for i in range(len(arr)-1, -1, -1):
            max_idx = i
            for j in range(i):
                if arr[max_idx] < arr[j]:
                    max_idx = j
            
            arr = arr[:max_idx+1][::-1] + arr[max_idx+1:]
            arr = arr[:i+1][::-1] + arr[i+1:]
            ks.append(max_idx+1)
            ks.append(i+1)
        
        return ks
        
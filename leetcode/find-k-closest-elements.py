class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        ind = bisect_left(arr, x)
        left = ind - 1
        right = ind + 1
        answer = []

        if ind < len(arr):
            if arr[ind] == x:
                answer = [arr[ind]]
                k -= 1

            else:
                right = ind
                left = ind - 1
        
        while left >= 0 and right < len(arr) and k > 0:
            
            if abs(arr[left] - x) <= abs(arr[right] - x):
                answer.append(arr[left])
                left -= 1

            else:
                answer.append(arr[right])
                right += 1
            
            k -= 1
        
        if k > 0 and left >= 0:
            answer.extend(arr[left - k + 1:left + 1  ])
        
        if k > 0 and right < len(arr):
            answer.extend(arr[right:right + k])
        
        return sorted(answer)
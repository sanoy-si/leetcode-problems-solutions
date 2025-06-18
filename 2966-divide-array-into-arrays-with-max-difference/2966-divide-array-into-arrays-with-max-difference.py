class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        def check():
            for arr in answer:
                if arr[-1] - arr[0] > k:
                    return False
                
            return True

        if len(nums) < 3 or len(nums) % 3:
            return []
            
        nums.sort()
        answer = []
        for i in range(0, len(nums), 3):
            answer.append(nums[i:i + 3])
        
        return answer if check() else []
 
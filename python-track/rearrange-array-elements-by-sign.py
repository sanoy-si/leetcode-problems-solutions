class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        positives = [num for num in nums if num > 0]
        negatives = [num for num in nums if num < 0]
        
        p = 0
        while p < len(nums)//2:
            ans.append(positives[p])
            ans.append(negatives[p])
            p += 1
        
        return ans

        
        
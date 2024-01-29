class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = []
        t = [0]
        
        for i in nums:
            t.append(t[-1] + i)
            
        t.append(0)

        for i in range(len(nums)):
            ans.append(abs(i * nums[i] - t[i]) + abs((len(nums) - i-1) * nums[i] - t[-2] + t[i+1]))

        return ans
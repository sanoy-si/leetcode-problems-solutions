class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_ = max(nums)
        counter = [0 for _ in range(max_ + 1)]
        for num in nums:
            counter[num] += 1
            
        for i in range(1, max_ + 1):
            for j in range(2 * i, max_ + 1, i):
                counter[i] += counter[j]
        
        for i in range(1, max_ + 1):
            counter[i] = counter[i] * (counter[i] - 1) // 2
        
        for i in range(max_, 0, -1):
            for j in range(2 * i, max_ + 1, i):
                counter[i] -= counter[j]
        
        for i in range(1, max_ + 1): 
            counter[i] += counter[i - 1]
        
        ans = []
        for i in queries:
            ans.append(bisect_left(counter, i + 1))
        
        return ans

        
        
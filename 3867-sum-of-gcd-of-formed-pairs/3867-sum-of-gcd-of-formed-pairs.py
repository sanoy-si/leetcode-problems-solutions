class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        max_ = nums[0]
        prefixGcd = []
        for num in nums:
            max_ = max(max_, num)
            prefixGcd.append(gcd(num, max_))
        
        prefixGcd.sort()
        left = 0
        right = len(prefixGcd) -1
        answer = 0
        while left < right:
            answer += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        
        return answer

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set()
        nums = set(nums)
        answer = 0

        def dfs(num):
            if num in visited or num not in nums:
                return 0
            visited.add(num)
            return 1 + dfs(num + 1) + dfs(num - 1)

        for num in nums:
            answer = max(dfs(num),answer)
        
        return answer
        
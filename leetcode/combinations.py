class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.combinations = []
        
        def dfs(num, combination):
            if len(combination) == k:
                self.combinations.append(combination[:])
                return
            
            if num > n:
                return 
            
            dfs(num + 1, combination[:])
            combination.append(num)
            dfs(num + 1, combination[:])
            
        dfs(1, [])

        return self.combinations
                
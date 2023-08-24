class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        
        def backtrack(i,combination):
            if len(combination) == k:
                combinations.append(combination[:])
                return 
            if i > n:return
            
            combination.append(i)
            backtrack(i+1,combination)
            
            combination.pop()
            
            backtrack(i+1,combination)
        backtrack(1,[])
        return combinations
        
                        
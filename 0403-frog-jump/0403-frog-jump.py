class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo = {}
        stones_set = set(stones)

        def dp(last, pos):
            if pos == stones[-1]:
                return True
            
            if pos not in stones_set:
                return False
            
            if (last, pos) not in memo:
                memo[(last, pos)] = False

                if last > 1:
                    if dp(last - 1, pos + last - 1):
                        memo[(last, pos)] = True
                
                if dp(last, pos + last):
                    memo[(last, pos)] = True
                
                if dp(last + 1, pos + last + 1):
                    memo[(last, pos)] = True

            return memo[(last, pos)]

        return dp(1, 1)

                

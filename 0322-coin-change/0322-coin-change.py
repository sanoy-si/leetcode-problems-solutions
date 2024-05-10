class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memory = {0:0}

        def dp(curr_amount):
            
            if curr_amount < 0:
                return inf

            if curr_amount not in memory:

                curr_count = inf
                for coin in coins:
                    curr_count = min(dp(curr_amount - coin) + 1 , curr_count)  

                memory[curr_amount] = curr_count

            return memory[curr_amount]


        answer = dp(amount)            

        return answer if answer != inf else -1
                

            

                
                
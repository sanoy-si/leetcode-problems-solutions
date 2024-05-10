class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memory = {0:0}

        def dp(curr_amount):

            if curr_amount < 0:
                return -1


            if curr_amount not in memory:

                curr_count = inf

                for coin in coins:
                    response = dp(curr_amount - coin)

                    if response != -1:
                        curr_count = min(response + 1 , curr_count)  

                if curr_count != inf:
                    memory[curr_amount] = curr_count

                else:
                    memory[curr_amount] = -1 

            return memory[curr_amount]

        return dp(amount)               

                

            

                
                
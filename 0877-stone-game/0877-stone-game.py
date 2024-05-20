class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = [[[-1 for _ in range(2)] for _ in range(len(piles))] for _ in range(len(piles))]

        def dp(left, right, turn):
            if left > right:
                return [0, 0]

            if left == right:
                if turn == 0:
                    return [piles[left], 0]
                
                else:
                    return [0, piles[left]]
            
            if memo[left][right][turn] == -1:

                if turn == 0:
                    left_alice, lfet_bob = dp(left + 1, right, 1)
                    right_alice, right_bob = dp(left, right - 1, 1)
                    memo[left][right][turn] = max([piles[left] + left_alice, lfet_bob], [piles[right] + right_alice, right_bob], key = lambda x: x[0] - x[1])
                
                else:
                    left_alice, lfet_bob = dp(left + 1, right, 0)
                    right_alice, right_bob = dp(left, right - 1, 0)
                    memo[left][right][turn] = max([left_alice, piles[left] +  lfet_bob], [right_alice, piles[right] +  right_bob], key = lambda x: x[0] - x[1])
              
            
            return memo[left][right][turn]
        
        alice_score, bob_score = dp(0, len(piles) - 1, 0)

        return alice_score > bob_score

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        sums = []
        for i in range(len(weights) - 1):
            sums.append(weights[i] + weights[i+1])
        
        sums.sort()

        return sum(sums[len(sums) - (k - 1):]) - sum(sums[:(k-1)])

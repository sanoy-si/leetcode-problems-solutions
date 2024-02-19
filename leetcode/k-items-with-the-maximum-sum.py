class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = min(numOnes, k)
        k -= numOnes

        if k <= 0:
            return ans

        k -= numZeros

        if k <= 0:
            return ans

        ans -= k

        return ans
        



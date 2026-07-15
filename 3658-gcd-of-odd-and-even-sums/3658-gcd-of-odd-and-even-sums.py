class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odds = evens =  0
        for i in range(1, 2 * n + 1):
            if i % 2:
                odds += i
            else:
                evens += i
            
        return gcd(evens, odds)
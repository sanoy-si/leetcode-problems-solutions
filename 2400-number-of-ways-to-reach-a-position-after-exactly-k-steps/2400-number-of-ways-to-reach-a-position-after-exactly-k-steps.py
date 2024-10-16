class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        diff = endPos - startPos
        MOD = int(1e9 + 7)

        if k < diff or (diff - k) % 2 != 0:
            return 0

        left_count = (diff - k) // -2
        right_count = k - left_count
        
        return (factorial(left_count + right_count) // (factorial(left_count) * factorial(right_count))) % MOD

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(1, int(sqrt(c)) + 1):
            diff_sqrt = sqrt(c - i ** 2)
            if int(diff_sqrt) == diff_sqrt:
                return True

        return False  
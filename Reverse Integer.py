class Solution:
    def reverse(self, x: int) -> int:
        if not -2 ** 31 <= x <= 2 ** 31:return 0
        if x>=0: 
            x = int(str(x)[::-1])
            return x if x <= 2 ** 31 else 0
        x=-int(str(x)[1:][::-1]) 
        return x if x >= -2 ** 31 else 0


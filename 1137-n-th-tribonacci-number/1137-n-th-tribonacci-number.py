class Solution:
    def tribonacci(self, n: int) -> int:
        memory = {0:0, 1:1, 2:1}

        def find_tribonacci(n):
            if n not in memory:
                memory[n] = find_tribonacci(n - 1) + find_tribonacci(n - 2) + find_tribonacci(n - 3)
            
            return memory[n]

        return find_tribonacci(n)
            

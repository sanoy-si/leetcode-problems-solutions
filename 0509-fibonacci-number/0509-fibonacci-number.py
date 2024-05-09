class Solution:

    def fib(self, n: int) -> int:
        memory = {0:0, 1:1}

        def func(n):
            if n in memory:
                return memory[n]
            
            memory[n] = func(n - 1) + func(n - 2)
            
            return memory[n]
        
        return func(n)

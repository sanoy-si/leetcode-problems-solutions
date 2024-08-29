class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        def get_factors(n):
            factors = set()

            for i in range(1, int(sqrt(n)) + 1):
               if n % i == 0:
                factors.add(i)
                factors.add(n / i)


            return factors

        factors = get_factors(n)

        factors = sorted(factors)
        
        if k <= len(factors):
            return int(factors[k - 1])
        
        return -1


        
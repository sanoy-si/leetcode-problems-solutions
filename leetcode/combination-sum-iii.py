class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = set(range(1, 10))
        combs = set()

        def func(comb, total, nums):
            if len(comb) == k and total == n:
                combs.add(tuple(sorted(comb[:])))
                return
            
            if len(comb) == k or total >= n:
                return
            
            new_nums = nums.copy()

            for num in nums:
                if n - (num + total) > (k - len(comb) - 1) * 9 or (n - num + total) < (k - len(comb) - 1) * 1:
                    continue
                      
                comb.append(num)
                new_nums.remove(num)
                func(comb, total + num, new_nums)

                new_nums.add(num)
                comb.pop()
        
        func([], 0, nums)

        return combs

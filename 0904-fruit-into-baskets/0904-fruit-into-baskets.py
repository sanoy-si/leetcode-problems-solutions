class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = defaultdict(int)
        max_fruit = 0
        left = 0
        
        for right in range(len(fruits)):
            counter[fruits[right]] += 1
            
            while len(counter) > 2:
                counter[fruits[left]] -= 1
                
                if counter[fruits[left]] == 0:
                    counter.pop(fruits[left])
                left += 1

            max_fruit  = max(max_fruit, right - left + 1)
        
        return max_fruit

        
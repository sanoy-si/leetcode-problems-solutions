class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        def check(mid):
            right = len(s) - 1
            left = mid - 1
            counter = Counter(s[:mid])
            target = Counter("aabbcc")
            while left >= 0 and ((counter["a"] < 2) or (counter["b"] < 2) or (counter["c"] < 2)):
                counter[s[right]] += 1
                counter[s[left]] -= 1
                left -= 1
                right -= 1
            
            return counter["a"] >= 2 and counter["b"] >= 2 and counter["c"] >= 2
        
        left = 6
        right = len(s)
        answer = -1
    
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                answer = mid
                right = mid - 1
            
            else:
                left = mid + 1
        
        return answer
        
                

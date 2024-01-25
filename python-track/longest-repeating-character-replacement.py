class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def find_length(ch, k):
            max_length = 0
            left = 0
            count = 0

            for right in range(len(s)):
                if s[right] != ch:
                    count += 1
                    
                while count > k:
                    if s[left] != ch:
                        count -= 1
                    left += 1
                    
                max_length = max(max_length, right - left + 1)
            
            return max_length
        

        return max([find_length(ch,k) for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
                    


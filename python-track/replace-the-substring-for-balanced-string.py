class Solution:
    def balancedString(self, s: str) -> int:
        current_counter = Counter(s)
        valid_count = len(s) // 4
        target_counter = Counter((['W'] * valid_count) + (['Q'] * valid_count) + (['E'] * valid_count) + (['R'] * valid_count))
        to_replace_counter = current_counter - target_counter


        if not to_replace_counter:
            return 0


        left = 0
        min_length = float('inf')
        window = Counter()

        for right in range(len(s)):
            window[s[right]] += 1
            
            while left <= right and not to_replace_counter - window:
                min_length = min(min_length, right - left + 1)
                
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    window.pop(s[left])
                left += 1
        
        return min_length


        
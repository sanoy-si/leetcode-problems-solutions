class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        left = 0
        length = 0
        
        for right in range(len(s)):
            counter [s[right]] += 1
            while right - left + 1 > len(counter):
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    counter.pop(s[left])
                left += 1
            
            length = max(length, right - left + 1)
        
        return length
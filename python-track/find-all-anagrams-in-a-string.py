class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_counter = Counter(p)
        window = Counter(s[:len(p)])
        left = 0

        ans = []
        if window == p_counter:
            ans.append(0)

        for right in range(len(p), len(s)):
            window[s[left]] -= 1
            if window[s[left]] == 0:
                window.pop(s[left])
            left += 1
            
            window[s[right]] += 1

            if window == p_counter:
                ans.append(left)
        
        return ans
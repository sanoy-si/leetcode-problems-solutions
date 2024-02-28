class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left = 0
        index = 0
        ans = []

        while index < len(s):
            max_idx = s.rindex(s[index])

            while index < max_idx and index < len(s):
                max_idx = max(max_idx, s.rindex(s[index]))
                index += 1
            
            
            ans.append(min(len(s) - left, index - left + 1))
            index += 1
            left = index
        
        return ans


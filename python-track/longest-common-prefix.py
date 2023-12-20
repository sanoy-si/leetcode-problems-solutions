class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for s in strs[1:]:
            l = min(len(ans),len(s))
            s = s[:l]
            ans = ans[:l]
            
            while s != ans and ans:
                ans = ans[:-1]
                s = s[:-1]

        
        return ans
            
        
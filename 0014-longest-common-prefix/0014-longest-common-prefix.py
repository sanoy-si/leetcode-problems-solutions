class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = min(strs,key = lambda x: len(x)) == 0
        if min(strs,key = lambda x: len(x)) == 0:
            return max(strs,key = lambda x: len(x)) == 0
        ans = ""
        for j in strs[0]:
            ans += j
            for i in strs:
                if not i.startswith(ans):
                    return ans[:-1]
        return ans
            
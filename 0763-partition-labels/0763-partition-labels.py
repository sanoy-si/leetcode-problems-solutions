class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        ans = []
        end = 0
        su = 0
        for i in range(len(s)):
            end = max(end, s.rindex(s[i]))
            if i == end:
                if not ans:ans.append(end + 1)
                else:ans.append(end - su + 1)
                end = 0
                su += ans[-1]

           
        return ans
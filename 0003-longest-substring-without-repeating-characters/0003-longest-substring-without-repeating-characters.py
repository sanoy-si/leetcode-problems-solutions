class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        cnt = 0
        ans = 0
        counter = {}
        for right in range(len(s)):
            if counter.get(s[right],0) == 0:
                counter[s[right]] = 1
            else:
                counter[s[right]]+=1
                while counter[s[right]] >1:
                    if counter.get(s[left],0) == 1:
                        counter.pop(s[left])
                    else:
                        counter[s[left]] -= 1
                    left += 1
                    cnt -= 1
            cnt += 1
            ans = max(cnt,ans)
        return ans
        
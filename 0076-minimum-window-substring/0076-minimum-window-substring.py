class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cs = Counter(s)
        ct = Counter(t)
        if ct - cs:
            return ''

        left = 0
        ans = s
        window = Counter('')

        for right in range(len(s)):
            if not window.get(s[right],0):
                window[s[right]] = 1
            else:
                window[s[right]] += 1

            while not (ct - window):
                if len(ans)>right-left+1:
                    ans=s[left:right+1]

                if window[s[left]]>1:
                    window[s[left]] -= 1

                else:
                    window.pop(s[left])
                left += 1
                
        return ans
             
        
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        se = set()
        ans = set()
        window = ""
        if len(s) < 10:
            return []
        for i in range(10):
            window += s[i]
        se.add(window)

        left = 0
        for right in range(i+1,len(s)):
            left += 1
            window = s[left:right+1]
            if window in se:
                if window not in ans:
                    ans.add(window)
            else:
                se.add(window)
        
        return ans



        
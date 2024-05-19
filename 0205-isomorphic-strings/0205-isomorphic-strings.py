class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_chars = {}
        t_chars = {}

        for i in range(len(s)):
            if (t[i] in t_chars and t_chars[t[i]] != s[i]) or (s[i] in s_chars and s_chars[s[i]] != t[i]):
                return False

            t_chars[t[i]] = s[i]
            s_chars[s[i]] = t[i]

        return True

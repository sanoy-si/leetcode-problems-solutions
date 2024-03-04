class Solution:
    def splitString(self, s: str) -> bool:

        def func(ind, parent):
            print(ind, parent)
            if ind == len(s):
                return True

            for i in range(ind + 1, len(s) + 1):
                if parent == int(s[ind:i]) + 1:
                    if func(i, int(s[ind:i])):
                        return True

            return False

        for i in range(1, len(s)):
            if func(i, int(s[:i])):
                return True
        
        return False
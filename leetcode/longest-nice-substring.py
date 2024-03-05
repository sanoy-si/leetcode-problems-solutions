class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        self.nice_string = ""

        def func(s):
            mid = -1
            counter = Counter(s)

            for i in range(len(s)):
                if s[i] == s[i].lower():
                    if s[i].upper() not in counter:
                        mid = i
                        break

                else:
                    if s[i].lower() not in counter:
                        mid = i
                        break
            
            if mid == -1:
                if len(self.nice_string) < len(s):
                    self.nice_string = s
                
                return
            
            func(s[:mid])
            func(s[mid + 1:])

        func(s)

        return self.nice_string
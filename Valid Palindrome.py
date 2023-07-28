class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s = list(filter(lambda x:97<=ord(x)<=122 or 48 <= ord(x) <= 57,s))
        return s == s[::-1]

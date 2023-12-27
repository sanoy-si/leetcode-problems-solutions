class Solution:
    def reverseWords(self, s: str) -> str:
        ls = [word.strip() for word in s.split()]
        return ' '.join(ls[::-1])
        
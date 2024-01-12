class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890']
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            
        return True

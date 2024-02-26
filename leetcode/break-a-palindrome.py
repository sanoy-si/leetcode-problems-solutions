class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        palindrome = list(palindrome)
        
        if palindrome.count('a') < len(palindrome) - 1:
            for i in range(len(palindrome)):
                if palindrome[i] != 'a':
                    palindrome[i] = 'a'
                    return ''.join(palindrome)


        for i in range(len(palindrome) - 1, -1, -1):
            if palindrome[i] != 'b':
                palindrome[i] = 'b'
                return ''.join(palindrome)
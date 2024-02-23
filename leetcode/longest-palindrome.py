class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        odd_count = 0

        for key, count in counter.items():
            if count % 2 == 1:
                odd_count += 1
        
        return len(s) - (odd_count - 1) if odd_count >= 1 else len(s)
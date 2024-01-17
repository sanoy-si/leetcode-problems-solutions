class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        for char in s[:k]:
            if char in 'aeiou':
                count += 1

        max_count = count
        left = 0
        for right in range(k, len(s)):
            if s[right] in 'aeiou':
                count += 1

            if s[left] in 'aeiou':
                count -= 1
            left += 1

            max_count = max(max_count, count)
        
        return max_count

        
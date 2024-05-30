class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        words_bit = [0 for _ in range(n)]

        for i, word in enumerate(words):
            for char in word:
                idx = ord(char) - ord('a')
                words_bit[i] |= 1 << idx
        
        max_product = 0
        for i in range(n):
            for j in range(i + 1, n):
                if words_bit[i] & words_bit[j] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        
        return max_product

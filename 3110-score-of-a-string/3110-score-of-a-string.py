class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            current_char_ascii = ord(s[i])
            next_char_ascii = ord(s[i + 1])
            score += abs(current_char_ascii - next_char_ascii)

        return score
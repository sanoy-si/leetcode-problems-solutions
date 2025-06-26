class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        def find_after_one(idx):
            nonlocal bit
            if len(s) - idx < len(bit):
                return len(s) - idx
            
            p = 0
            count = 0
            while p < len(bit) and idx < len(s):
                if bit[p] == s[idx]:
                    p += 1
                    idx += 1
                    count += 1
                
                elif bit[p] == '1':
                    return min(len(s) - idx + count, len(bit))

                else:
                    while idx < len(s) and s[idx] != '0':
                        idx += 1
            
            if p == len(bit):
                return len(bit) 
            
            return len(bit) - 1


        zeros_before = {}
        count = 0
        for i in range(len(s)):
            if s[i] == '0':
                count += 1

            else:
                zeros_before[i] = count

        bit = bin(k)[2:]
        answer = 0
        bit_length = k.bit_length()
        for i in range(len(s)):
            if s[i] == '1':
                answer = max(answer, zeros_before[i] + find_after_one(i))

        return max(answer, s.count('0'))
                
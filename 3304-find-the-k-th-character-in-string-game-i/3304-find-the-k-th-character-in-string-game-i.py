class Solution:
    def kthCharacter(self, k: int) -> str:
        def function(level, shift, idx):
            if level == 0:
                return shift

            curr_length = 2 ** level
            if idx > curr_length // 2:
                return function(level - 1, shift + 1, idx - curr_length // 2)
            return function(level - 1, shift, idx)
            
        shift = function(ceil(log2(k)), 0, k)
        return chr(97 + (shift % 26))
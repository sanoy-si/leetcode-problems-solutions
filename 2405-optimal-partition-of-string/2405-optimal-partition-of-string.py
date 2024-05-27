class Solution:
    def partitionString(self, s: str) -> int:
        window_chars = set()
        partition_count = 1

        for i, char in enumerate(s):
            if char in window_chars:
                partition_count += 1
                window_chars = set(char)
            
            else:
                window_chars.add(char)
        
        return partition_count


        
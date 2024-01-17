class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        operation = 0
        for color in blocks[:k]:
            if color == 'W':
                operation += 1
        
        min_operation = operation
        left = 0
        for right in range(k, len(blocks)):
            if blocks[right] == 'W':
                operation += 1
            if blocks[left] == 'W':
                operation -= 1
            left += 1

            min_operation = min(min_operation, operation)
        
        return min_operation
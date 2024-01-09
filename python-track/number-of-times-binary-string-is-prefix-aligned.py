class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_flip = 0
        sequential_correct = 0
        count = 0
        flipped = set()
        
        for flip in flips:
            flipped.add(flip)
            max_flip = max(max_flip, flip)
            while sequential_correct + 1 in flipped:
                sequential_correct += 1
            if max_flip == sequential_correct:
                count += 1

        return count
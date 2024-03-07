class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        ind = bisect_right(letters, target)

        if ind < len(letters):
            return letters[ind]
        
        return letters[0]


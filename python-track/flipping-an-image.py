class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        image = [[0 if i else 1 for i in row[::-1]] for row in image]
        return image
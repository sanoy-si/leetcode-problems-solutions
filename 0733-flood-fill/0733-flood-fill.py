class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        colo  = image[sr][sc]
        self.visited = set()
        self.directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(row,col):
            if (row,col) not in self.visited and 0 <= row and row < len(image) and 0 <= col and col < len(image[0]) and image[row][col] == colo:
                self.visited.add((row,col))
                image[row][col] = color
                for nrow,ncol in self.directions:
                    dfs(row+nrow,col+ncol)
        dfs(sr,sc)
        return image
        
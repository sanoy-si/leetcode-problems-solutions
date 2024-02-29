# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dict = defaultdict(list)

        def dfs(node, row, col):
            if node:
                self.dict[col].append((row, node.val))
                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)

        items = list(self.dict.items())
        items.sort(key = lambda x: x[0])

        
        answer = [value for key, value in items]
        
        for i in range(len(answer)):
            answer[i].sort()
            
            for j in range(len(answer[i])):
                answer[i][j] = answer[i][j][1] 
      
        return answer

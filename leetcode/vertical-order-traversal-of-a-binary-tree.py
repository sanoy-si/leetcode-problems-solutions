# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        tuples = []

        def dfs(node, row, col):
            if node:
                tuples.append((col, row, node.val))
                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)

        tuples.sort()
        answer = []
        p = 0

        while p < len(tuples):
            col = tuples[p][0]
            temp = []

            while p < len(tuples) and col == tuples[p][0]:
                temp.append(tuples[p][-1])
                p += 1

            answer.append(temp)

      
        return answer

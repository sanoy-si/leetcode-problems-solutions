# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = Counter()
        
        def dfs(node):
            if not node:
                return 

            counter[node.val] += 1

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        max_count = max(counter.values())

        answer = []
        for key in counter.keys():
            if counter[key] == max_count:
                answer.append(key)
        
        return answer
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = []
        flag = True
        queue = deque([root]) 
        
        while queue:
            level = []

            for i in range(len(queue)):
                node = queue.pop()

                level.append(node.val)

                if node.left:
                    queue.appendleft(node.left)

                if node.right:
                    queue.appendleft(node.right)

            if flag:
                levels.append(level)
                flag = False

            else:
                levels.append(level[::-1])
                flag = True
        
        return levels

            

        
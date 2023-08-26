# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        lst =[[root.val]]
        queue = deque()
        queue.append(root)
        level = 0

        while queue:
            temp =[]

            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    temp.append(curr.left.val)
                    queue.append(curr.left)
                if curr.right:
                    temp.append(curr.right.val)
                    queue.append(curr.right)
            if temp:
                lst.append(temp)
        return lst
            
                
        
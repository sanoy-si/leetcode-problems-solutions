# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        queue = deque()
        queue.append(root)
        lst = [root.val]
        while queue:
            temp = 101
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    temp = curr.left.val

                if curr.right:
                    queue.append(curr.right)
                    temp =  curr.right.val   
            if -100<=temp<=100:lst.append(temp)
        return lst
        
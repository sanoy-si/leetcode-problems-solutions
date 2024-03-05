# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
             
        max_ind = max(range(len(nums)), key = lambda x: nums[x])
        node = TreeNode(nums[max_ind])
        node.left = self.constructMaximumBinaryTree(nums[:max_ind])
        node.right = self.constructMaximumBinaryTree(nums[max_ind + 1:])

        return node
        
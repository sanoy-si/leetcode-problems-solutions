# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def merge_two_sorted_arrays(left, right):
            p1 = p2 = 0
            merged_arr = []
            while p1 < len(left) and p2 < len(right):
                
                if left[p1] <= right[p2]:
                    merged_arr.append(left[p1])
                    p1 += 1
                
                else:
                    merged_arr.append(right[p2])
                    p2 += 1
                
            if left[p1:]:
                merged_arr += left[p1:]
            
            if right[p2:]:
                merged_arr += right[p2:]

            return merged_arr

        answer = 0
        def dfs(node, depth):
            nonlocal answer
            if not node:
                return []

            if not node.left and not node.right:
                return [depth]
            
            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)
            
            p1, p2 = 0, len(right) - 1
            while p1 < len(left) and p2 >= 0:
                curr_distance = left[p1] - depth + right[p2] - depth
                if curr_distance <= distance:
                    answer += p2 + 1
                    p1 += 1

                else:
                    p2 -= 1 
            
            return merge_two_sorted_arrays(left, right)
            
        dfs(root, 0)
        return answer



            

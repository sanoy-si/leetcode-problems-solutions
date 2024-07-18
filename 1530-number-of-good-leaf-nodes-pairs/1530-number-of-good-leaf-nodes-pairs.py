# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        answer = 0
        def dfs(node, depth):
            nonlocal answer

            if not node:
                return []

            if not node.left and not node.right:
                return [depth]
            
            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)
            
            merged_arr = []
            p1 = p2 = 0

            if left and right:
                curr_distance = left[p1] - depth + right[p2] - depth
                while curr_distance <= distance:
                    left_val = left[p1]
                    left_ans = 0
                    while p1 < len(left) and left[p1] == left_val:
                        left_ans += 1
                        p1 += 1
                    
                    right_val = right[p2]
                    right_ans = 0
                    while p2 < len(right) and right[p2] == right_val:
                        right_ans += 1
                        p2 += 1

                    answer += max(left_ans, right_ans)
                    curr_distance = left[p1] - depth + right[p2] - depth if p1 < len(left) and p2 < len(right) else inf
            
            p1 = p2 = 0
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

        
        dfs(root, 0)
        return answer



            

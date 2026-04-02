# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (True, 0)
            r = dfs(node.right)
            l = dfs(node.left)
            return (r[0] and l[0] and abs(r[1]-l[1]) <= 1, max(r[1], l[1]) + 1) 
        return dfs(root)[0]

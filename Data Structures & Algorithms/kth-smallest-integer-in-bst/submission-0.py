# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node, k):
            if not node:
                return None, k
            
            
            val, k = dfs(node.left, k)
            if val is not None:
                return val, k
            k -= 1
            if k == 0:
                return node.val, k
            return dfs(node.right, k)
        return dfs(root, k)[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxLen = 0

        def dfs(node):

            if not node:
                return 0
            
            leftVal = dfs(node.left)
            rightVal = dfs(node.right)

            self.maxLen = max(self.maxLen, leftVal + rightVal)
            return 1 + max(leftVal, rightVal)

        dfs(root)
        return self.maxLen
        
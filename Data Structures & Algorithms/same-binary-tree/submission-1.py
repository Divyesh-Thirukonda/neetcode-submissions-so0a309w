# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def bfs(node):
            if not node:
                return ['null']
            left = bfs(node.left)
            right = bfs(node.right)
            curr = [node.val]
            return curr + left + right
        l1 = bfs(p)
        l2 = bfs(q)
        return l1 == l2
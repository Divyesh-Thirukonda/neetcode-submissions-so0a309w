# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # keep track of answer / counter
        self.count = 0

        def dfs(maxForThisPath, node):
            if not node:
                return

            newMaxForThisPath = maxForThisPath
            if node.val >= maxForThisPath:
                self.count += 1
                print(node.val)
                newMaxForThisPath = node.val

            leftV = dfs(newMaxForThisPath, node.left)
            rightV = dfs(newMaxForThisPath, node.right)

            return

        dfs(root.val, root)
        return self.count

#    [3]
#    /\
#   [3]
#   /\
# [4][2]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        

        right_sub_tree = self.maxDepth(root.right)
        left_sub_tree = self.maxDepth(root.left)

        return 1 + max(left_sub_tree, right_sub_tree)

        # Time: O(n)
        # Space: O(h)
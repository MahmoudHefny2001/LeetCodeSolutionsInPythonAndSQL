# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def doDepthFirstSearch(node, maxValue):
            if not node:
                return 0
            
            result = 1 if node.val >= maxValue else 0
            
            maxValue = max(maxValue, node.val)
            
            result += doDepthFirstSearch(node.right, maxValue)
            result += doDepthFirstSearch(node.left, maxValue)
            
            return result
        
        return doDepthFirstSearch(root, root.val)
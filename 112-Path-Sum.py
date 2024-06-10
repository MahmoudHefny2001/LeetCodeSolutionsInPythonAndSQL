# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        

        def doDepthFirstSearch(node, currentSum):
            if not node:
                return False
            
            currentSum += node.val

            if not node.left and not node.right:
                return currentSum == targetSum

            return (doDepthFirstSearch(node.right, currentSum) or doDepthFirstSearch(node.left, currentSum))
        

        return doDepthFirstSearch(root, 0)
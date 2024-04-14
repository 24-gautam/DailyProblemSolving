# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root : 
            self.sumOfLeftLeaves(root.left) 
            if self.isLeaf(root.left) : self.res += root.left.val 
            self.sumOfLeftLeaves(root.right) 
        
        return self.res 
    
    def isLeaf(self, root) : 
        return False if not root or (root.right or root.left) else True 
         
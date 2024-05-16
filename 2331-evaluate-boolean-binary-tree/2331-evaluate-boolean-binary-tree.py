# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root : 
            self.evaluateTree(root.left)
            self.evaluateTree(root.right)
            if self.notLeaf(root) : 
                if root.val == 2 : 
                    root.val = root.left.val | root.right.val 
                else : root.val = root.left.val & root.right.val 
            
        if root : return root.val

    def notLeaf(self, root) : 
        return root and root.left and root.right
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = False 
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if root : 
            if self.isValidPath(head, root) : return True
            self.res |= self.isSubPath(head , root.left) 
            self.res |= self.isSubPath(head , root.right) 

        return self.res 
    
    def isValidPath(self, head, root) : 
        if head == None : return True 
        if root == None : return False 

        flag = False 
        if root.val == head.val : 
            flag |= self.isValidPath(head.next , root.left) 
            flag |= self.isValidPath(head.next , root.right) 

        return flag
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        while head : 
            next = head.next 
            head.next = prev 
            prev = head 
            head = next 
        
        while prev : 
            n , temp = prev.val , prev.next
            while temp and temp.val < n : 
                temp = temp.next 

            prev.next = temp 

            next = prev.next 
            prev.next = head
            head = prev 
            prev = next 

        return head  
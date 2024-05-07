# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head , newHead , carry = self.rev(head) , None , 0 

        while head : 
            t = carry if not head else carry + 2 * head.val 
            head.val = t % 10  
            carry = t // 10 

            next = head.next 
            head.next = newHead 
            newHead = head 
            head = next 

        if carry > 0 : 
            newHead = ListNode(carry , newHead) 
        
        return newHead

    def rev(self, head) : 
        prev = None 
        while head : 
            next = head.next 
            head.next = prev 
            prev = head 
            head = next 
        return prev 
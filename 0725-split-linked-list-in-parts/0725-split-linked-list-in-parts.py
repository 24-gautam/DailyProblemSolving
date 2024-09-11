# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n , res = self.length(head) , []
        partSize = n // k 
        extra = n % k 

        while k : 
            curr = head
            prev = curr
            t = partSize 

            while t and curr: 
                prev = curr
                curr = curr.next 
                t -= 1 

            if extra and curr : 
                prev = curr 
                curr = curr.next 
                extra -= 1
            
            if prev : prev.next = None 
            res.append(head) 
            head = curr 
            k -= 1 

        return res 

    
    def length(self , head) : 
        if not head : return 0 
        return 1 + self.length(head.next)
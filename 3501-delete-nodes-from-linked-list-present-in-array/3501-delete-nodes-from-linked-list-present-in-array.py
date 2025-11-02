# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums) 
        newHead = ListNode()
        newHead.next = head   
        dummy = newHead 

        while dummy and dummy.next : 
            if dummy.next.val in nums : 
                temp = dummy
                while temp.next and temp.next.val in nums : 
                    temp = temp.next 
                dummy.next = temp.next
            dummy = dummy.next
        
        return newHead.next
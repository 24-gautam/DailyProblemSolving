# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums) 
        temp = ListNode(0 , head) 
        newHead = temp 

        while temp : 
            t1 = temp.next
            while t1 and t1.val in nums : t1 = t1.next 
            temp.next = t1 
            temp = temp.next 

        return newHead.next 

        

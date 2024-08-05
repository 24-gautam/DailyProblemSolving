# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        firstCrit , prev , head , i , prevCrit , currCrit , minCritDis = -1 , head , head.next , 0 , -1 , -1 , 1e9

        while head.next : 
            if head.val > prev.val  and head.val > head.next.val : 
                if firstCrit == -1 : 
                    firstCrit , currCrit = i , i
                else : prevCrit , currCrit = currCrit , i 

            if head.val < prev.val and head.val < head.next.val : 
                if firstCrit == -1 : 
                    firstCrit , currCrit = i , i
                else : prevCrit , currCrit = currCrit , i 

            i += 1

            if prevCrit >= 0 : minCritDis = min(minCritDis , currCrit - prevCrit)
            prev , head = head , head.next


        return [-1 , -1] if prevCrit < 0 else [minCritDis , currCrit - firstCrit]
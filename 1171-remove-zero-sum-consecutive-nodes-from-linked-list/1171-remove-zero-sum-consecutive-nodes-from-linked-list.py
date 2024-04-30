# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead , temp , l , s , i = ListNode(0) , head , [] , 0 , 0

        while temp : 
            l.append(temp.val) 
            temp , s = temp.next , s + temp.val 

        while i < len(l) : 
            t = 0 
            for j in range(i , len(l)) : 
                t += l[j] 
                if not t : 
                    l[i:j+1] , i = [0] * (j + 1 - i) , j
                    break
            i += 1 
        
        k , temp = 0 , newHead 

        while k < len(l) : 
            if l[k] != 0 : 
                temp.next = ListNode(l[k])
                temp = temp.next 
            k += 1 
        
        return newHead.next 
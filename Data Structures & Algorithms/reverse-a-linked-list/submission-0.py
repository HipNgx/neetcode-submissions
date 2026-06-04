# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        prv = None
        while p :
            nextNode = p.next
            p.next = prv
            prv = p
            p = nextNode
        return prv

        

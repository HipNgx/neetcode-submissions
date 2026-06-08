# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p = l1
        q = l2
        dummy = ListNode(0)
        head = dummy
        Carry = 0
        while p or q or Carry :
            val = Carry
            if p :
                val += p.val
                p = p.next
            if q :
                val += q.val
                q = q.next
            if Carry == val :
                dummy.next = ListNode(Carry)
                Carry //= 10
            else :
                Carry = val // 10
                new = val % 10
                dummy.next = ListNode(new)
            dummy = dummy.next
        return head.next


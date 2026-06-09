# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        p = head
        res = []
        prv = None
        count_ = 1
        while p and count_ <= right :
            if count_ >= left :
                res.append(p.val)
            else :
                prv = p
            p = p.next
            count_ += 1
        if prv :
            for i in res[::-1] :
                n = ListNode(i)
                prv.next = n
                prv = prv.next
            prv.next = p
            return head
        else :
            dummy = ListNode(0)
            head1 = dummy
            for i in res[::-1] :
                n = ListNode(i)
                dummy.next = n
                dummy = dummy.next
            dummy.next = p
            return head1.next


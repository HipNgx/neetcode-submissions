# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        newList = []
        p = head
        while p :
            newList.append(p.val)
            p = p.next
        mid = len(newList)//2
        half1 = newList[:mid:]
        half2 = newList[mid:][::-1]
        res = []
        for i in range(len(half2)):       # ✅ dùng len(half2) để không bỏ sót
            if i < len(half1):
                res.append(half1[i])
            res.append(half2[i])
        dummy = ListNode(0)
        p = head
        for val in res:
            p.val = val                   # ✅ sửa trực tiếp node gốc
            p = p.next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []   # ✅ trả về list rỗng

        left  = self.inorderTraversal(root.left)   # [trái]
        mid   = [root.val]                          # [gốc]
        right = self.inorderTraversal(root.right)  # [phải]

        return left + mid + right  # ✅ gộp lại
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
            # Hàm hỗ trợ tính độ cao
            def get_height(node):
                if not node:
                    return 0
                return 1 + max(get_height(node.left), get_height(node.right))
            
            # Nếu cây rỗng, nó cân bằng
            if not root:
                return True
            
            # Kiểm tra độ cao trái và phải
            left = get_height(root.left)
            right = get_height(root.right)

            return abs(left-right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

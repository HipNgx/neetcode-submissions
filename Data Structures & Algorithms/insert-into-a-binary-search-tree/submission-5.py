# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None : 
            root = TreeNode(val)
            return root
        if root.val > val :
            if root.left is None :
                p = TreeNode(val)
                root.left = p
                return root
            self.insertIntoBST(root.left, val)
        elif root.val < val :
            if root.right is None :
                p = TreeNode(val)
                root.right = p
                return root
            self.insertIntoBST(root.right, val)
        else :
            return -1
        return root
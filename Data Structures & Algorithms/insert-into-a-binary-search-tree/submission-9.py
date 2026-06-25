# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root :
            return TreeNode(val)
        p = root
        while p :
            if p.val < val :
                if not p.right :
                    p.right = TreeNode(val)
                    break
                p = p.right
            else :
                if not p.left :
                    p.left = TreeNode(val)
                    break
                p = p.left
        return root
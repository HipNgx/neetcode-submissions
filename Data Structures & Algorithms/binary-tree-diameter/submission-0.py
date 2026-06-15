# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(node):
            if not node:
                return 0
            
            # 1. Get the max depth of left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 2. Update the global maximum diameter found so far
            # (edges = left depth + right depth)
            self.max_diameter = max(self.max_diameter, left + right)
            
            # 3. Return the height of the current node to its parent
            return 1 + max(left, right)

        dfs(root)
        return self.max_diameter
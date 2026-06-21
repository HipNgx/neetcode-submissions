# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : 
            return []
        q = []
        res = []

        q.append(root)
        cur_level = 0
        while q :
            res.append([])
            for _ in range (len(q)) :
                node = q.pop(0)
                res[cur_level].append(node.val)
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
            cur_level += 1
        return res

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        bfs = self.levelOrder(root)
        res = []
        for i in bfs :
            res.append(i[-1])
        return res
        
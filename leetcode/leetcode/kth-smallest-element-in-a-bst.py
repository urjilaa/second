# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = [0]
        Found = False
        save = [0]

        def find(node,n, Found, save):
            if not Found and node.left:
                find(node.left, n, Found, save)
                
            n[0] += 1
            if n[0] == k:
                save[0] = node.val
                Found = True

            if not Found and node.right:
                find(node.right, n, Found, save)

        find(root, n, Found, save)
        return save[0]
        




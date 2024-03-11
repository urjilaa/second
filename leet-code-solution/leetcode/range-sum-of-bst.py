# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = []
        def increasing(root):
            if root:
                increasing(root.left)
                ans.append(root.val)
                increasing(root.right)
        increasing(root)

        s = 0
        for i in range(len(ans)):
            if ans[i] >= low and ans[i] <= high:
                s += ans[i]
                
        return s  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(int)
        def mode(node):
            #nonlocal d
            if node.left:
                mode(node.left)

            d[node.val] += 1

            if node.right:
                mode(node.right)

        mode(root)  
        mx = max(d.values())
        res = []
        for key, val in d.items():
            if val == mx:
                res.append(key)
        
        return res
        
    
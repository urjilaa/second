# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list) 
        #finding every values at every level       
        def helper(node, level):
            if node:
                helper(node.left, level+1)
                helper(node.right, level+1)
                d[level].append(node.val)                
        helper(root, 0)
        #print(d)

        key = sorted(d)
        lst = []
        for i in key:
            lst += [d[i]]
        #print(lst)

        for i in range(len(lst)):
            if i%2 != 0:
                lst[i] = lst[i][::-1]
        
        return lst
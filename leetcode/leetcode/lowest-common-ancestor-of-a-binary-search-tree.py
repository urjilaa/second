# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lst_p = []
        lst_q = []

        def ancestor(tree, node, lst):
            if not tree:
                return

            if node.val == tree.val:
                lst.append(tree.val)
                return

            if node.val < tree.val:
                lst.append(tree.val)
                ancestor(tree.left, node, lst)
            else:
                lst.append(tree.val)
                ancestor(tree.right, node, lst)

        ancestor(root, p, lst_p)
        ancestor(root, q, lst_q)
        
        mn = TreeNode()
        l = 0
        r = 0

        while l < len(lst_p) and r < len(lst_q):
            if lst_q[r] == lst_p[l]:
                mn.val = lst_p[l]
            l+= 1
            r+=1

        return mn
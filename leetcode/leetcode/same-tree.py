# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(node1, node2):
            if not node1 and not node2:
                return True

            if (not node1 and node2) or (node1 and not node2):
                return False
                
            if node1.val != node2.val:
                return False
            else:
               return same(node1.left, node2.left) and same(node1.right, node2.right) 
            
        return same(p, q)

        # lst1 = []
        # lst2 = []
        # def Traverse(node, lst):
        #     if node.left:
        #         Traverse(node.left, lst)
        #     else:
        #         Traverse(node.right, lst)
        # Traverse(p, lst1)
        # Traverse(q, lst2)
        
        # return lst1 == lst2
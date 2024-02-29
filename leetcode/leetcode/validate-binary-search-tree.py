# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #res = [True, float('-inf'), float('-inf')]
        def check(node):
            
            res = [True, float('-inf'), float('inf')]
            if not node.left and not node.right:
                #res = [True,max(node.val, res[1]), min(node.val, res[2])]
                res[0] = True
                res[1] = max(node.val, res[1]) #res[1]== max value
                res[2] = min(node.val, res[2]) #res[2] == min value
                return res
            
            if node.left:
                temp = check(node.left)
                #check if our temp[0] the value before this 
                #node.val(new max) > temp[1](inital max)
                #res[0](initail boolean val)
                res[0] = temp[0] and (node.val > temp[1]) and res[0]

                res[1] = max(temp[1], res[1])
                res[1] = max(node.val, res[1])

                res[2] = min(temp[2], res[2])
                res[2] = min(node.val, res[2])

            if node.right:
                temp = check(node.right)
                res[0] = temp[0] and (node.val < temp[2]) and res[0]

                res[1] = max(temp[1], res[1])
                res[1] = max(node.val, res[1])

                res[2] = min(temp[2], res[2])
                res[2] = min(node.val, res[2])

            return res

        return check(root)[0] #we only need to return the boolean value
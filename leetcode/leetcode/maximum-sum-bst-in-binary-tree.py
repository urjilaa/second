# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        mx = [0]
        def check(node):
            res = [True, float('-inf'), float('inf'), node.val]

            if not node.left and not node.right:
                res[1] = node.val #res[1] == max value
                res[2] = node.val #res[2] == min value
                
            if node.left:
                temp = check(node.left)
                #check if our temp[0] the value before this 
                #node.val(new max) > temp[1](initial max)
                #res[0](initail boolean val)
                res[0] = temp[0] and (node.val > temp[1])
                res[1] = max(node.val, temp[1])
                res[2] = min(node.val, temp[2])
                res[3] += temp[3]

            if node.right:
                temp = check(node.right)
                res[0] = temp[0] and (node.val < temp[2]) and res[0]
                
                res[1] = max(temp[1], res[1])
                res[1] = max(node.val, res[1])

                res[2] = min(temp[2], res[2])
                res[2] = min(node.val, res[2])

                res[3] += temp[3]

            if res[0]:
                mx.append(res[3])

            return res

        check(root)
        return max(mx)
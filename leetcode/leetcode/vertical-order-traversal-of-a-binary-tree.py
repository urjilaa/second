# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        my_dict = defaultdict(list)
        x = [0]
        y = [0]
        def traversal(nood, x, y):
            my_dict[x[0]].append([y[0], nood.val])
            if nood.left:
                x[0] -= 1
                y[0] += 1
                traversal(nood.left, x, y)
                y[0] -= 1 
                x[0] += 1
           
            if nood.right:
                x[0] += 1
                y[0] += 1
                traversal(nood.right, x, y)
                y[0] -= 1 
                x[0] -= 1 
                  
        traversal(root, x, y)

        for key in my_dict.keys():
            my_dict[key].sort()

        #print(my_dict)
        key = sorted(my_dict)
        ans = []
        for i in key:
            temp = [c[1] for c in my_dict[i]]
            ans.append(temp)
        

        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def divide_and_conquer(left, right):
            if left > right:
                return 
            if left == right:
                return TreeNode(nums[left])
            
            mid = (left+right)//2

            root = TreeNode(nums[mid])

            left_arr = divide_and_conquer(left, mid-1) #arr[:mid]
            right_arr = divide_and_conquer(mid+1, right)  #arr[mid+1:]
            
            root.left = left_arr
            root.right = right_arr
        
            return root
        return divide_and_conquer(0, len(nums)-1)    

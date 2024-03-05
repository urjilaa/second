class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visted = set()
        def backtrack(nums):
            res.append(nums)
            visted.add(tuple(nums))
            for i in range(len(nums)-1):
                arr = nums[:]
                arr[i], arr[i+1] = arr[i+1], arr[i] 
                if  tuple(arr) not in visted:                    
                    backtrack(arr)

        backtrack(nums)
        return res
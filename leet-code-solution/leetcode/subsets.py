class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def sets(first_nums, lst):
            if len(lst) <= len(nums):
                ans.append(lst[:])

            for i in range(first_nums,len(nums)):
                lst.append(nums[i])
                sets(i+1, lst)
                lst.pop()
            
        sets(0, [])
        return ans

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        lst = []
        def backtrack(start_idx):
            ans.append(lst[:])

            for i in range(start_idx,len(nums)):
                lst.append(nums[i])
                backtrack(i+1)
                lst.pop()
            
        backtrack(0)
        return ans

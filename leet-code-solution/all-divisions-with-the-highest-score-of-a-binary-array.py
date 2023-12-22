class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeros = [0] * len(nums)
        ones = [0] * (len(nums)+1)
        count_zeros = 0
        count_ones = 0

        for i in range(len(nums)):
            zeros[i] = count_zeros
            if nums[i] == 0:
                count_zeros += 1
        zeros.append(count_zeros)
       
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == 1:
                count_ones += 1
            ones[j] = count_ones
        
        new_lst = []
        ans = []
        for i in range(len(nums) + 1):
            new_lst.append(ones[i] + zeros[i])
        m = max(new_lst)
        for j in range(len(new_lst)):
            if new_lst[j] == m:
                ans.append(j)
        return ans    

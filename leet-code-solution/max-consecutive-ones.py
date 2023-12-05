class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        new_count=0
        l=0
        r=0
        
        while r<len(nums):
            if nums[r]==1:
                count+=1
                r+=1
            else:
                l=r+1
                r+=1
                new_count=max(new_count,count)
                count=0
                
        return max(new_count,count)
            
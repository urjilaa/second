class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
           # elif nums[mid] < nums[right]:                
           #     right = mid - 1
           #the above won't work since the mid point can be the answer
           #so we have to move our right pointer to mid not mid-1
            else:
                right = mid
                
        return nums[left]
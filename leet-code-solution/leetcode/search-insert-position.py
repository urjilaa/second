class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #return bisect_left(nums, target)
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1       
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return left
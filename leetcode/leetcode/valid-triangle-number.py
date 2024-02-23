class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)-1, -1, -1):
            l = 0
            r = i-1
            while l<r:
                summ = nums[l] + nums[r]
                if summ > nums[i]:
                    res += r - l
                    r -= 1
                else:
                    l += 1
                
        return res

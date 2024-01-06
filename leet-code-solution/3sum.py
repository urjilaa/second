class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        #target = 0 ???

        for i in range(len(nums)):
            #target = 0 - nums[i]
            l = i + 1
            r = len(nums)-1

            while l < r:
                if nums[l] + nums[r] > -nums[i]:
                    r -= 1
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    res.add((nums[i],nums[l],nums[r]))
                    l += 1
                    r -= 1

        return list(map(list, res))
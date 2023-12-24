class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        x = float('inf')
        y = float('inf')

        for i in range(len(nums)):
            if nums[i] <= x:
                x = nums[i]
                print(x)
            elif nums[i] <= y:
                y = nums[i]
                print(y)
            else:
                return True

        return False            
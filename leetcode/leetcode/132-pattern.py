class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stacks = []
        k = float('-inf')
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < k:
                return True
            while stacks and nums[i] > stacks[-1]:
                k = stacks.pop()
               
            stacks.append(nums[i])

        return False

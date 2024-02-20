class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        n = len(nums)

        for i in range(n):
            if i > jump or jump > n-1:
                break
            jump = max(jump, i + nums[i])
            print(jump)
        
        return jump >= n-1

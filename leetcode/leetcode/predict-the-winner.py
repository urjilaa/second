class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def play(left, right):
            if left == right:
                return nums[left]
            
            left_count = nums[left] - play(left+1, right)
            right_count = nums[right] - play(left, right-1)

            return max(left_count, right_count)
        return play(0, len(nums)-1) >= 0
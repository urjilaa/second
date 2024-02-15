class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        ans  = 0
        left = 0
        odd = 0

        for r in range(len(nums)):
            if nums[r] % 2!= 0:
                count += 1
                odd = 0
            while count == k:
                odd += 1
                if nums[left] %2 != 0:
                    count -= 1
                left +=1
            ans += odd
            
        return ans        
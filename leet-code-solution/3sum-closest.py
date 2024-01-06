class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        add = []
        diff = []

        for i in range(len(nums)):
            l = i+1
            r = len(nums) - 1

            while l < r:
                tot = nums[i] + nums[l] + nums[r]
                if tot < target:
                    add.append(tot)
                    l += 1
                elif tot > target:
                    add.append(tot)
                    r -= 1
                else:
                    return tot

        for j in range(len(add)):
            diff.append(abs(target - add[j]))
            
        m = min(diff)
        for i in range(len(diff)):
            if diff[i] == m:
                return add[i]
        #print(add)
        #print(diff)
        #print(min(diff))
        
        #return add[j]
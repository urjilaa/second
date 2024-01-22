class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        prefix = 0
        count = 0

        for i in range(len(nums)):
            prefix += nums[i]
            count += d[prefix - goal]
            d[prefix] += 1

        return count

        # if we use d = {} instead of defaultdict(int)
            #prefix += nums[i]
            #if prefix - goal in d:
            #    count += d[prefix - goal]
            #    print(count)

            #if prefix in d:
            #    d[prefix] += 1
            #else:
            #    d[prefix] = 1
            #    print(d)

        


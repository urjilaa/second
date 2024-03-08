class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uniq = set(nums)
        hash_map = defaultdict(int)
        count = 0
        l = 0
        for r in range(len(nums)):
            hash_map[nums[r]] += 1
            while len(hash_map) == len(uniq) and l <= r:
                count += (len(nums)-r)
                print(count, r)
                hash_map[nums[l]] -= 1
                if hash_map[nums[l]] == 0:
                    del hash_map[nums[l]]
                l += 1

        return count
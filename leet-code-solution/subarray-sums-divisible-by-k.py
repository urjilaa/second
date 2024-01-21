class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        count = 0
        prefix = 0
        for num in nums:
            prefix += num
            count += d[prefix % k]
            d[prefix % k] += 1
        return count
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = defaultdict(int)
        hash[0] = 1
        tot = 0
        count = 0
        for num in nums:
            tot += num
            count += hash[tot-k]
            hash[tot] += 1
        return count

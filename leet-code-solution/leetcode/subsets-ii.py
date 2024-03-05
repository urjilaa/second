class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        comb = []
        def bk(idx):
            res.add(tuple(comb[:]))
            for i in range(idx, len(nums)):
                comb.append(nums[i])
                print(comb, 1111)
                bk(i+1)
                print(comb, 2222)
                comb.pop()
                print(comb, 3333)
        bk(0)
        return res
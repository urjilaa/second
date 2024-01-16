class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        nw = []
        for i in range(len(nums)):
            i = sum(nums[:i+1])
            nw.append(i)
            
        return nw
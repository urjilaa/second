class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        list1 = {}
        for i in range(len(nums)):
            list1[nums[i]] = i
        for i in range(len(operations)):
            idx = list1.get(operations[i][0])
            nums[idx] = operations[i][1]
            list1.pop(operations[i][0])
            list1[operations[i][1]] = idx
            
        return nums
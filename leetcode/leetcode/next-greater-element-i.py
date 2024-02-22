class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i in nums1:
            d[i] = -1
        stacks = []
        for i in range(len(nums2)):
            while stacks and stacks[-1] in d and stacks[-1] < nums2[i]:
                x = stacks.pop()
                d[x] = nums2[i]
            stacks.append(nums2[i])
            
        ans = []
        for i in nums1:
            if i in d:
                ans.append(d[i])
        return ans
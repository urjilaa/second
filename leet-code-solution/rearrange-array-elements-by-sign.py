class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        

        for i in nums:
            if i >= 0:
                positive.append(i)
            else:
                negative.append(i)

        rearrange_array = []
        for pos, neg in zip(positive, negative):
                rearrange_array.append(pos)
                rearrange_array.append(neg)
                
        return rearrange_array
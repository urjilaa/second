class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        min_p = []
        max_p = []
        pivots=[]

        for i in nums:
            if i < pivot:
                min_p.append(i)
            elif i > pivot:
                max_p.append(i)
            else:
                pivots.append(i)
        
        return min_p + pivots + max_p
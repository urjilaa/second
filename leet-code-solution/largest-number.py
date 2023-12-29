class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def custom_sort(x):
            return str(x)*100
            
        nums = sorted(nums, key=custom_sort, reverse=True)
        st = "".join(map(str, nums))
        
        return str(int(st))  # To remove leading zeros
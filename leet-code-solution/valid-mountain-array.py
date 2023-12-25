class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2 or max(arr) == arr[0] or max(arr) == arr[len(arr)-1]:
            return False

        l = 0
        r = len(arr) - 1
        while arr[l] < arr[l + 1]:
            l += 1
   
        while arr[r] < arr[r - 1]:
            r -= 1
            
        return r == l
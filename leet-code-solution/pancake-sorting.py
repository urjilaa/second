class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        n = len(arr)

        def flip(arr, k, n):
            arr = arr[:k+1][::-1] + arr[k+1:]
            arr = arr[:n][::-1] + arr[n:]
            return arr
        
        while n>1:
            k = arr.index(n)
            ans.append(k+1)
            arr = flip(arr, k, n)
            ans.append(n)
            n -= 1

        return ans



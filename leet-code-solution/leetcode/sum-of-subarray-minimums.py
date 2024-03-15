class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        right = [len(arr)-1]*len(arr)
        left = [0]*len(arr)
        stack = []
        l , r , ans  = 0 , 0 , 0
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                 val = stack.pop()
                 right[val] = i - 1
            if stack:
                left[i] = stack[-1] + 1
            stack.append(i)
        for i in range(len(arr)):
            l = i - left[i] + 1
            r = right[i] - i + 1
            ans +=   arr[i]*l*r
        return ans  % (10**9 + 7)
       
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dec = deque()
        ans = []
        for i in range(k):
            while dec and dec[-1][0] < nums[i]:
                dec.pop()
            dec.append([nums[i], i])
        ans.append(dec[0][0])
        
        for j in range(k, len(nums)):
            if dec and j - dec[0][1] == k:
                dec.popleft()
            while dec and dec[-1][0] < nums[j]:
                dec.pop()
            dec.append([nums[j], j])
            ans.append(dec[0][0])

        return ans

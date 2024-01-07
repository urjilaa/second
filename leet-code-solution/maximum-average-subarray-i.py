class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #res = []
        #i = 0

        #while i+k < len(nums):
        #    s = sum(nums[i:i+k])/float(k)
        #    res.append(s)
        #    print(s, res, len(res))
        #    s -= nums[i]
        #    s += nums[i+k]
        #    i += 1
        
        #for i in range(len(res)):
        #    return max(res[i])
        l = 0
        r = k
        avg = 0.0
        
        for i in range(k):
            avg += nums[i] / k
        
        max_avg = avg
        while r < len(nums):
            avg -= nums[l] / k
            avg += nums[r] / k
            max_avg = max(max_avg, avg)
            l += 1
            r += 1
        return max_avg

        #m = list(map(int, res))
        #print(m)
        #n = max(m)
        #for i in range(len(m)):
        #    if m[i] == n:
        #        return res[i]
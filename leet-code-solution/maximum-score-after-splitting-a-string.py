class Solution:
    def maxScore(self, s: str) -> int:
        t = len(s)-1
        tot = 0
        zero_count = [0]*t
        one_count = [0]*t
        curr_count = 0
        for i in range(t):
            if s[i] == '0':
                curr_count += 1
            zero_count[i] = curr_count
       
        curr_count = 0
        for j in range(t,0,-1):
            if s[j] == '1':
                curr_count += 1
            one_count[j-1] = curr_count
        mx = 0
        for i in range(t):
            mx = max(mx, zero_count[i] + one_count[i])
        return mx
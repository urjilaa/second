class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int) 
        even = 0
        odd = 0

        for i in s:
            d[i] += 1

        for i in d:
            if d[i]%2 == 0:
                even += d[i]
            else:
                even += d[i] - 1
                odd = 1
        
        return even + odd
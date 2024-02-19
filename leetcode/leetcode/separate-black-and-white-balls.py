class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        s1 = list(s)
        left = 0
        right = n-1
        count = 0

        while left < right:
            if s1[left] == '0':
                left += 1
            elif s1[right] == '1':
                right -= 1
            else:
                s1[left],s1[right] = s1[right],s1[left] 
                count += (right - left)
                left += 1
                right -= 1
            
        return count
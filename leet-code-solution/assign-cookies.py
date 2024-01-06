class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        i = len(g)-1
        j = len(s)-1
        count = 0
        if len(s) == 0:
            return 0

        while i >= 0 and j >= 0:
            if s[j] >= g[i]:
                count += 1
                i -= 1
                j -= 1
            else:
                i -= 1
                
        return count

        #for i in range(len(g)-1, -1, -1):
        #    for j in range(len(s)-1, -1, -1):
        #        if g[i] <= s[j]:
        #            i += 1

        #return i

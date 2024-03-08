class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] = i
            else:
                d[s[i]] = i
        
        res = []
        size, end = 0, 0
        for i in range(len(s)):
            size += 1
            end = max(d[s[i]], end)
            if end == i:
                res.append(size)
                size = 0
        
        return res


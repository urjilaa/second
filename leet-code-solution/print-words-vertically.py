class Solution:
    def printVertically(self, s: str) -> List[str]:
        s=s.split()
        m = len(max(s, key=lambda x: len(x)))
        ans = [""]*m
        for i in range(m):
            for j in range(len(s)):
                if i<len(s[j]):
                    ans[i] += s[j][i]
                else:
                    ans[i] += " "
            ans[i]=ans[i].rstrip()
        return ans

        
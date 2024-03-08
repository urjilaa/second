class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        lst = [""]
        def solve(s):
            st = set(s)
            if len(s) == 1:
                return

            flage = True
            for i in range(len(s)):
                if s[i].swapcase() not in st:
                    flage = False
                    break
                   
            if flage:
                lst.append(s)
            else:
                solve(s[:i])
                if i+1 < len(s):
                    solve(s[i+1:])

        solve(s)
        lst.sort(key=len, reverse=True)
        return lst[0]
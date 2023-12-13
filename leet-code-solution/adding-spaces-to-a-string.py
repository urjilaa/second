class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i = 0
        ans = []
        
        for j in spaces:
            ans.append(s[i: j])
            i = j
        ans.append(s[i:])

        return " ".join(ans)


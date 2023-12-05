class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        m=min(len(word1), len(word2))

        for i in range(m):
            ans += word1[i]
            ans += word2[i]
        ans+=word1[m:]
        ans+=word2[m:]
        return ans
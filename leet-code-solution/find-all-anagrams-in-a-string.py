class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        n = len(p)
        p_dict = Counter(p)
        s_dict = Counter(s[:n])

        i = 0
        j = n - 1
        while j < len(s):
            if p_dict == s_dict:
                res.append(i)
            s_dict[s[i]] -= 1
            if s_dict[s[i]] == 0:
                del s_dict[s[i]]
            i += 1
            j += 1
            if j < len(s):
                s_dict[s[j]] += 1
        
        return res
                
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #strs.sort(int, key=len(strs))
        if strs is None or len(strs)==0:
            return ""
        prefix=strs[0]
        for i in strs:
            while i.find(prefix) != 0:
                prefix=prefix[:-1]
                if not prefix:
                    return ""
        return prefix
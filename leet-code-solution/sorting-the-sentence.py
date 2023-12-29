class Solution:
    def sortSentence(self, s: str) -> str:
        d = {}
        new_s = list(map(str, s.split()))
        
        lst = []
        for i in new_s:
           d[int(i[-1])] = i[:len(i)-1]
        lst[:]= d.keys()
        lst.sort()
        
        dd = []
        for i in lst:
            dd.append(d[i])        
        
        return " ".join(dd)
                
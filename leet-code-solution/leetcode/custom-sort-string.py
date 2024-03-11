class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order = list(order)
        s = list(s)
        lst = []
        for i in order:
            for j in s[:]:
                if i == j:
                    lst.append(i)
                    s.remove(j)
        lst += s
        return ''.join(lst)
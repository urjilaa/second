class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sort = sorted(zip(heights,names))
        lst = []

        for i,j in sort:
            lst.append(j)
        return lst[::-1]
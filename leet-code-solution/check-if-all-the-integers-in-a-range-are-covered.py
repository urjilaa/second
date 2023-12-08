class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        checker ={i for i in range(left, right+1)}
        element = set()

        for x, y in ranges:
            element.update(range(x, y+1))

        if checker <= element:
            return True
            
        return False
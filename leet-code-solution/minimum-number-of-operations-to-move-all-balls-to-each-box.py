class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = []

        for index in range(n):
            tot = 0
            for l in range(index - 1, -1, -1):
                if boxes[l] == "1":
                    tot += index - l
            for r in range(index +1, n):
                if boxes[r] == "1":
                    tot += r - index
            ans.append(tot)
        
        return ans
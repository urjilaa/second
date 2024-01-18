class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0]*1001
        for pp, start, end in trips:
            arr[start] += pp
            arr[end] -= pp
        
        p = 0
        for i in arr:
            p += i
            if p > capacity:
                return False
        return True
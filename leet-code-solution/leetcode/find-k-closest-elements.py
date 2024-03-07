class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.append(float('inf'))
        left, right = -1, len(arr) #take both at offset pt
        d = {arr[i]:abs(x-arr[i]) for i in range(len(arr))}
        
        while left + 1 < right:
            mid = (left+right)//2
            if arr[mid] <= x:
                left = mid
            else:
                right = mid
        
        res = []
        while k > 0:
            if left >= 0 and d[arr[left]] <= d[arr[right]]:
                res.append(arr[left])
                left -= 1
                k -= 1
            elif right < len(arr) and d[arr[left]] > d[arr[right]]:
                res.append(arr[right])
                right += 1
                k -= 1

        return sorted(res)

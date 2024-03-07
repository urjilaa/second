class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        lst = []
        lst2 = []
        for i in range(len(intervals)):
            lst.append([intervals[i][0], i]) 
            lst2.append(intervals[i][1]) 
        lst.append([float('inf'), -1])    
        lst.sort()
        print(lst)
        
        ans = []
        for i in lst2:
            left, right = -1, len(lst)-1
            
            while left + 1 < right:
                mid = (left+right)//2
                if lst[mid][0] < i:
                    left = mid
                else:
                    right = mid
            ans.append(lst[right][1])
                
        return ans
        
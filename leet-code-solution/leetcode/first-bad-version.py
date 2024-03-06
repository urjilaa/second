# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n 
        #we start l from 0 to takecare if our min ans is on fist idx(l) and we are returning r idx
        while l +1 < r: 
            mid = (l+r)//2
            if isBadVersion(mid):    
                r = mid
            elif not isBadVersion(mid): 
                l = mid
        
        return r

            
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] *(n+1)
        for booking in bookings:
            first, last,seats = booking
            res[first-1] +=seats
            res[last] -= seats
        
        #do its prefix 
        for i in range(1,len(res)):
            res[i] += res[i-1]
            #prefix = 0
            #prefix += res[i-1]
            #res[i] += prefix
            #print(prefix)

        res.pop()
        return res

        
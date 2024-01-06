class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        l = 0
        r = len(people)-1
        if people[0] + people[1] > limit:
            return len(people)
        #if people[r] == limit:
        #    count += 1
        
        while l <= r:
            if people[l] + people[r] > limit: 
                r -= 1
            else:
                l += 1
                r -= 1
            count += 1
        return count     

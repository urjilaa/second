class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        i = 0

        #only runs if tickets[k](our target element) is defferent from 0
        while tickets[k] > 0:
            #only runs if element at i idx is different from 0
            if tickets[i] != 0:
                tickets[i] -= 1
                time += 1
            i += 1
            
            #i idx will be equal to the len(tickets) after it run the last idx
            #which is the time to restart the process again
            if i == len(tickets):
                i = 0
        
        return time 
                

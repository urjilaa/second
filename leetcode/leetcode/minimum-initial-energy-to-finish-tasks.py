class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: (x[0]-x[1],-x[1]))
        sums = 0
        y =tasks[0][1]
        sums += y
        for i in tasks:
            if i[1]>y:
                sums += i[1]-y
                y += i[1]-y
            y -= i[0]
                
    
        return sums
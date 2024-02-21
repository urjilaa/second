class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        mul = 0
        oper = 0
        ans = 0
        
        while mul < maxDoubles and target != 1:
            if target % 2 == 0:
                target = target // 2 
                mul += 1
            else:
                target -= 1 
                oper += 1
                target = target//2
                mul += 1
                
        ans = oper + target-1 + mul
        return ans
                

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win, lose = zip(*matches)
        x = sorted(set(win) - set(lose)) 
        y = sorted(k for k, v in Counter(lose).items() if v == 1)
        
        return [x, y]

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        set1 = set(fronts + backs)
        
        for x, y in zip(fronts, backs):
            if x == y:
                set1.discard(x)
        
        return min(set1, default = 0)

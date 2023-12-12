class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [''] * len(indices)
        
        for letter, ind in zip(s, indices):
            ans[ind] = letter
            
        return ''.join(ans)
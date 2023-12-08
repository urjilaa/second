class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index={}
        
        for index, val in enumerate(order):
            order_index[val] = index

        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]) or order_index[words[i][j]] > order_index[words[i+1][j]]: 
                    return False
                if order_index[words[i][j]] < order_index[words[i+1][j]]: 
                    break

        return True
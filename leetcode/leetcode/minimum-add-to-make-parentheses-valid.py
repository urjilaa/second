class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        s1 = list(s)
        count_open = 0
        count = 0

        if len(s) == 0:
            return 0

        for i in s1:
            if i == '(':
                count_open += 1
            if i == ')':
                if count_open >= 1:
                    count_open -= 1
                else:
                    count += 1
            
        return (count + count_open)
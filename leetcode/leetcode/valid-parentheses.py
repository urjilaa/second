class Solution:
    def isValid(self, s: str) -> bool:
        stacks = []
        d = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in d:
                if stacks and d[i] == stacks[-1]:
                    stacks.pop()
                else:
                    return False
            else:
                stacks.append(i)

        return not stacks
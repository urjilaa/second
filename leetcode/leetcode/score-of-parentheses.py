class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stacks = [0]
        for char in s:
            if char == "(":
                stacks.append(0)

            else:
                temp = stacks.pop()
                stacks[-1] += max(2*temp, 1)
        return stacks[-1]
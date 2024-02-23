class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums_stacks = []
        for token in tokens:
            # we also used len(token)>1 since token.isnumeric() will be False for negative numbers
            if len(token)>1 or token.isnumeric(): 
                nums_stacks.append(int(token))
                #print(nums_stacks)
            else:
                if token == "+":
                    nums_stacks[-2] += nums_stacks[-1]
                elif token == "-":
                    nums_stacks[-2] -= nums_stacks[-1]
                elif token == "*":
                    nums_stacks[-2] *= nums_stacks[-1]
                else:
                    nums_stacks[-2] = int(nums_stacks[-2] / nums_stacks[-1])
                nums_stacks.pop()

        return nums_stacks[0] #we need to return the value not the list
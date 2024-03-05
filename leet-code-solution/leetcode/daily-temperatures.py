class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stacks = []
        for i in range(len(temperatures)):
            while stacks and temperatures[stacks[-1]] < temperatures[i]:
                idx = stacks.pop()
                print(idx)
                ans[idx] = i - idx
            stacks.append(i)
        return ans
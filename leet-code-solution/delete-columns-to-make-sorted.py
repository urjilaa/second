class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):

            for  r in range(1, len(strs)):
                if strs[r-1][i] > strs[r][i]:
                    count += 1
                    break

        return count

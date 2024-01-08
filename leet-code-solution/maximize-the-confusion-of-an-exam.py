class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        best = 0

        for correct in ["T", "F"]:
            opp_count = 0 # is number of the opposit things inside l, r, inclusive
            l = 0

            for r in range(n):
                if answerKey[r] != correct:
                    opp_count += 1
                while opp_count > k:
                    if answerKey[l] != correct:
                        opp_count -= 1
                    l += 1

                best = max(best, r - l + 1)
        return best
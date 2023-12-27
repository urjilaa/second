class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        sums = 0
        n_term = 0
        count = 0

        for n in flips:
            sums += n
            n_term = max(n_term, n)
            
            if sums == int((n_term/2)*(1+n_term)):
                count += 1

        return count



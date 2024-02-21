class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        s = Counter(answers)
        print(s)
        ans = 0
        for key, val in s.items():
            
            if key == 0:
                ans += val
                print(val)
            if key != 0:
                n = 1
                while n*(key+1) < val:
                    n += 1
                    print(n)
                ans += n*(key+1)
                #print(n*(key+1))
                print(n*(key+1), val)
        return ans
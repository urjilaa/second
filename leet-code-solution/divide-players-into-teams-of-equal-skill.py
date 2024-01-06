class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill) - 1

        res = 0
        target = sum(skill)/(len(skill)/2)
        #print(2(sum(skill)/len(skill))) why does it not work?
      
        while l < r:
            if skill[l] + skill[r] == target:
                res += skill[l] * skill[r]
                l += 1
                r -= 1
            else:
                return -1
            
        return res

        
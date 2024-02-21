class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0
        count10 = 0

        for i in bills:
            if i == 5:
                count5 += 1
            if i == 10:
                if count5 >= 1:
                    count10 += 1
                    count5 -= 1
                else:
                    return False
            if i == 20:
                if count5 >= 1 and count10 >= 1:
                    count5 -= 1
                    count10 -= 1
                elif count5 >= 3:
                    count5 -= 3
            
                else:
                    return False
            
        return True
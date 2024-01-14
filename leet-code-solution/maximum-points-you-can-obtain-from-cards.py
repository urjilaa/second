class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints)
        left, right = k-1, size-1

        currentPick = sum(cardPoints[:k])
        maxPoints = currentPick

        for i in range(k):
            currentPick+= (cardPoints[right] - cardPoints[left])
            maxPoints = max(maxPoints, currentPick)
            left = left-1
            right = right-1

        return maxPoints

            

        #left = 0
        #right = len(cardPoints) - 1
        #s = 0
        #count = 0

        #while left < right:
         #   if cardPoints[left] < cardPoints[right]:
         #       s += cardPoints[right]
          #      right += 1
          #      count += 1
           # elif cardPoints[left] == cardPoints[right]:
            #    s += cardPoints[right]
             #   left += 1
             #   right += 1
             #   count += 1
            #else:
             #   while count < k:
             #       s += cardPoints[left]
              #      left += 1
               #     count += 1
            #left += 1
            #right += 1
#        return s
        


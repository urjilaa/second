class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        print(deck, 1111)

        sdeck = deque([i for i in range(n)])
        #print(sdeck, 222)
        lookup = [None] * n
        #print(lookup, 3333)
        t = 0
        m = len(sdeck)

        while len(sdeck) > 0:
            top = sdeck.popleft()
            lookup[top] = t
            t += 1
            #print(top, lookup[top], 44444)

            if len(sdeck) > 0:
                top = sdeck.popleft()
                sdeck.append(top)
                #print(sdeck, top)
        ans = [ 
            deck[lookup[i]] for i in range(n) 
        ]
        #print(ans, 55555)
        return ans
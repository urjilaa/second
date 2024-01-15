class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d = defaultdict(list)
        min_len = float('inf')

        for i in range(len(cards)):
            d[cards[i]].append(i)

        for key in d:
            ans = d[key]
            for i in range(1, len(ans)):
                min_len = min(min_len, ans[i] - ans[i-1] + 1)
                
        return -1 if min_len == float('inf') else min_len
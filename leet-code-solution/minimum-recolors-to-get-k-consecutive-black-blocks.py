class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        c = Counter(blocks[:k])
        w_count = c['W']
        min_w = w_count
        print(w_count)
        for j in range(k,len(blocks)):
            if blocks[j] == 'W':
                w_count += 1
            if blocks[j-k] == 'W':
                w_count -= 1
            min_w = min(min_w, w_count)
        return min_w

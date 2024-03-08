def solve():
    n = int(input())
    dist = list(map(int, input().split()))
    speed = list(map(int, input().split()))

    def calc(point):
        t = float('-inf')
        for i in range(n):
            t = max(t, abs(point - dist[i])/speed[i])
        return t

    l = min(dist)
    r = max(dist)

    cnt = 500
    while cnt:
        mid1 = l +(r-l)/3
        mid2 = r - (r-l)/3

        val1 = calc(mid1)
        val2 = calc(mid2)

        if val1 == val2:
            l = mid1
            r = mid2
        elif val1 > val2:
            l = mid1
        else:
            r = mid2
        cnt -= 1

    print(calc(mid1))

# t = int(input())
t = 1
for _ in range(t):
    solve()
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
i = 2
while i < n:
    if a[i] + k <= 5:
        ans += 1
    i += 3
print(ans)
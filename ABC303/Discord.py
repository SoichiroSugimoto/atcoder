N, M = list(map(int, input().split()))
a = [input().split() for i in range(M)]
len = int(N * (N - 1) // 2)
cnt = 0
pool = []

for m in range(M):
    for n in range(N):
        if (n == 0):
            continue
        else:
            if (pool.count([a[m][n - 1], a[m][n]]) + pool.count([a[m][n], a[m][n - 1]]) == 0):
                pool.append([a[m][n - 1], a[m][n]])
                cnt += 1
print(int(len) - cnt)

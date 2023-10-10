H, W = list(map(int, input().split()))
A = [list(input()) for i in range(H)]
B = [list(input()) for i in range(H)]
s = 0
t = 0
i = 0
j = 0

for s in range(H):
    for t in range(W):
        ok = 1
        for i in range(H):
            for j in range(W):
                if (A[(i - s + H) % H][(j - t + W) % W] != B[i][j]):
                    ok = 0
        if (ok == 1):
            print('Yes')
            exit()
print('No')
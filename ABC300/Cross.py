H, W = list(map(int, input().split()))
C = [list(input()) for i in range(H)]
res = [0] * H

for i in range(H):
    for j in range(W):
        n = 0
        if (C[i][j] == '#'):
            while (i - n >= 0 and i + n < H and j - n >= 0 and j + n < W):
                if (C[i - n][j - n] != '#' or C[i - n][j + n] != '#' or C[i + n][j - n] != '#' or C[i + n][j + n] != '#'):
                    break
                n += 1
            if (n > 1):
                res[n - 2] += 1
print(" ".join(map(str, res)))

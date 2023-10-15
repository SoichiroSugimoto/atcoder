H, W = list(map(int, input().split()))
S = [list(input()) for i in range(H)]

for j in range(H):
    for i in range(W):
        if (i + 4 < W and S[j][i] + S[j][i + 1] + S[j][i + 2] + S[j][i + 3] + S[j][i + 4] == 'snuke'):
            print(j + 1, i + 1)
            print(j + 1, i + 2)
            print(j + 1, i + 3)
            print(j + 1, i + 4)
            print(j + 1, i + 5)
        elif (j + 4 < H and S[j][i] + S[j + 1][i] + S[j + 2][i] + S[j + 3][i] + S[j + 4][i] == 'snuke'):
            print(j + 1, i + 1)
            print(j + 2, i + 1)
            print(j + 3, i + 1)
            print(j + 4, i + 1)
            print(j + 5, i + 1)
        elif (i - 4 >= 0 and S[j][i] + S[j][i - 1] + S[j][i - 2] + S[j][i - 3] + S[j][i - 4] == 'snuke'):
            print(j + 1, i + 1)
            print(j + 1, i)
            print(j + 1, i - 1)
            print(j + 1, i - 2)
            print(j + 1, i - 3)
        elif (j - 4 >= 0 and S[j][i] + S[j - 1][i] + S[j - 2][i] + S[j - 3][i] + S[j - 4][i] == 'snuke'):
            print(j + 1, i + 1)
            print(j, i + 1)
            print(j - 1, i + 1)
            print(j - 2, i + 1)
            print(j - 3, i + 1)
        elif (i + 4 < W and j + 4 < H and S[j][i] + S[j + 1][i + 1] + S[j + 2][i + 2] + S[j + 3][i + 3] + S[j + 4][i + 4] == 'snuke'):
            print(j + 1, i + 1)
            print(j + 2, i + 2)
            print(j + 3, i + 3)
            print(j + 4, i + 4)
            print(j + 5, i + 5)
        elif (i + 4 < W and j - 4 >= 0 and S[j][i] + S[j - 1][i + 1] + S[j - 2][i + 2] + S[j - 3][i + 3] + S[j - 4][i + 4] == 'snuke'):
            print(j + 1, i + 1)
            print(j, i + 2)
            print(j - 1, i + 3)
            print(j - 2, i + 4)
            print(j - 3, i + 5)
        elif (i - 4 >= 0 and j + 4 < H and S[j][i] + S[j + 1][i - 1] + S[j + 2][i - 2] + S[j + 3][i - 3] + S[j + 4][i - 4] == 'snuke'):
            print(j + 1, i + 1)
            print(j + 2, i)
            print(j + 3, i - 1)
            print(j + 4, i - 2)
            print(j + 5, i - 3)
        elif (i - 4 >= 0 and j - 4 >= 0 and S[j][i] + S[j - 1][i - 1] + S[j - 2][i - 2] + S[j - 3][i - 3] + S[j - 4][i - 4] == 'snuke'):
            print(j + 1, i + 1)
            print(j, i)
            print(j - 1, i - 1)
            print(j - 2, i - 2)
            print(j - 3, i - 3)

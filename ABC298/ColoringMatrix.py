N = int(input())
A = [list(map(int, input().split()))  for i in range(N)]
B = [list(map(int, input().split()))  for i in range(N)]
f = 0

r_A = []
for r in range(4):
    tmp_f = f
    if (r_A != []):
        A = r_A
        r_A = []
    for i in range(N):
        r_a = []
        for j in range(N):
            if (A[N - j - 1][i] == 1):
                if (B[i][j] != 1):
                    f += 1
                r_a.append(1)
            else:
                r_a.append(0)
        r_A.append(r_a)
    if (tmp_f == f):
        print('Yes')
        exit()
print('No')

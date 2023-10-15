N, M, H ,K = list(map(int, input().split()))
S = input()
items = [list(map(int, input().split())) for i in range(M)]
used_items = []
p = [0, 0]
cnt = 0

for s in S:
    if (s == 'U'):
        p[1] += 1
    elif (s == 'D'):
        p[1] -= 1
    elif (s == 'R'):
        p[0] += 1
    elif (s == 'L'):
        p[0] -= 1
    H -= 1
    if (H < 0):
        print('No')
        exit()
    if (p not in used_items and p in items):
        if (H < K):
            used_items.append([p[0], p[1]])
            H = K
    cnt += 1
    if (cnt >= N):
        print('Yes')
        exit()

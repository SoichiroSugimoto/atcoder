H, W = list(map(int, input().split()))
S = [input() for i in range(H)]


result = []
for s in S:
    r = ''
    n = 0
    for i in range(W):
        if (i + n + 1 < W and s[i + n] == 'T' and s[i + n + 1] == 'T'):
            r += 'PC'
            n += 1
        elif (i + n < W):
            r += s[i + n]
    print(r)

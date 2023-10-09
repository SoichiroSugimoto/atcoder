N = int(input())
S = input()

if (S.count('o') == 0 or S.count('-') == 0):
    print(-1)
else:
    max_cnt = 0
    for i in range(N):
        cnt = 0
        while (i < N and S[i] == 'o'):
            cnt += 1
            i += 1
        if (max_cnt < cnt):
            max_cnt = cnt
        if (max_cnt > N - i - 1):
            break
    print(max_cnt)

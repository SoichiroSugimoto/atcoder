N, A, B = list(map(int, input().split()))
C = list(map(int, input().split()))

for i in range(N):
    if (A + B == C[i]):
        print(i + 1)
        exit()

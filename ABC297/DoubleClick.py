N, D = list(map(int, input().split()))
T = list(map(int, input().split()))

for i in range(N - 1):
    if (i == 0):
        continue
    elif (T[i] - T[i - 1] <= D):
        print(T[i])
        exit()
print(-1)

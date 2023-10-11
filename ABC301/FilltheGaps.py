N = int(input())
A = list(map(int, input().split()))
res = []

for i in range(N):
    n = 1
    res.append(A[i])
    while (i + 1 < N and A[i] > A[i + 1] and A[i] - n > A[i + 1]):
        res.append(A[i] - n)
        n += 1
    while (i + 1 < N and A[i] < A[i + 1] and A[i] + n < A[i + 1]):
        res.append(A[i] + n)
        n += 1

print(" ".join(map(str, res)))

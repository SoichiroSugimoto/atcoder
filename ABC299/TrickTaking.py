N, T = list(map(int, input().split()))
C = list(map(int, input().split()))
R = list(map(int, input().split()))

if (C.count(T) > 0):
    clr = T
else:
    clr = C[0]

max = 0
max_val = 0
for i in range(len(C)):
    if (C[i] == clr):
        if (max_val < R[i]):
            max_val = R[i]
            max = i

print(max + 1)
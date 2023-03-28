nm = list(input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
N = int(nm[0])
M = int(nm[1])
Ak = []
Bk = []
Ck = []
C = A
store = 0

for b in B:
  for i in range(N + M):
    j = store + i
    if (N <= 0):
      break
    if (0 < b and b < C[0]):
      Bk.append(1)
      C.insert(0, b)
      store = j
      break
    elif (C[j] < b and b < C[j + 1]):
      Bk.append(j + 2)
      C.insert(j + 1, b)
      store = j
      break
    elif (C[-1] < b):
      Bk.append(len(C) + 1)
      C.insert(-1, b)
      store = j
      break

for i in range(N + M + 1):
  if (i > 0):
    Ck.append(i)

Ak = list(set(Ck) - set(Bk))
ans_A = ' '.join(map(str, Ak))
ans_B = ' '.join(map(str, Bk))
print(ans_A)
print(ans_B)

nm = list(input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
N = int(nm[0])
M = int(nm[1])
Ak = []
Bk = []
Ck = []
C = A


for b in B:
  for i in range(len(C)):
    if (0 < b and b < C[0]):
      Bk.append(1)
      C.insert(0, b)
      break
    elif (C[i] < b and b < C[i + 1]):
      Bk.append(i + 2)
      C.insert(i + 1, b)
      break
    elif (C[-1] < b):
      Bk.append(len(C) + 1)
      C.insert(-1, b)
      break

for i in range(len(C) + 1):
  if (i > 0):
    Ck.append(i)

Ak = list(set(Ck) - set(Bk))
ans_A = ' '.join(map(str, Ak))
ans_B = ' '.join(map(str, Bk))
print(ans_A)
print(ans_B)

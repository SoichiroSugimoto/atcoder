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
    print(j, " / ", N + M)
    if (b > C[0] and len(Bk) == 0):
      Ak.append(j + 1)
    if (0 < b and b < C[0]):
      print("(1)------", j, store, " / ", j - store)
      Bk.append(1)
      C.insert(0, b)
      store = j
      break
    elif (C[j] < b and b < C[j + 1]):
      print("(2)------", j + 2, store + 2, " / ", j - store)
      for n in range(j - store - 1):
        Ak.append(n + j + 1)
      Bk.append(j + 2)
      C.insert(j + 1, b)
      store = j
      break
    elif (C[-1] < b):
      print("(3)------", j, store, " / ", j - store)
      Bk.append(len(C) + 1)
      C.insert(-1, b)
      store = j
      break
    # print(j)

print(N + M - len(C))

for i in range(N + M - len(C) + 1):
  Ak.append(len(C) + i)

# Ak = list(set(Ck) - set(Bk))
ans_A = ' '.join(map(str, Ak))
ans_B = ' '.join(map(str, Bk))
print(ans_A)
print(ans_B)

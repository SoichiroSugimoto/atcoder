NM = list(map(int, input().split()))
V = [list(map(int, input().split()))  for i in range(NM[1])]

# print(V)
p =  [0 for i in range(NM[0])]

for v in V:
  p[v[0] - 1] += 1
  p[v[1] - 1] += 1

# print(NM[0], NM[1], p)

if (p.count(1) == 2 and p.count(2) == NM[0] - 2):
  print("Yes")
else:
  print("No")
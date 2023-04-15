N, M = map(int, input().split())
V = [list(map(int, input().split())) for i in range(M)]

def find(parent, x):
  if (parent[x] == x):
    return x
  return find(parent, parent[x])

def union(parent, x, y):
  x_root = find(parent, x)
  y_root = find(parent, y)
  parent[x_root] = y_root

def same(parent, x, y):
  return find(parent, x) == find(parent, y)

parent = [i for i in range(N)]
p = [0 for i in range(N)]

for v in V:
  union(parent, v[0] - 1, v[1] - 1)
  p[v[0] - 1] += 1
  p[v[1] - 1] += 1

conn = 0
for i in range(N):
  if (same(parent, parent[0], parent[i])):
    conn += 1

if (conn == N and p.count(1) == 2 and p.count(2) == N - 2):
  print("Yes")
else:
  print("No")

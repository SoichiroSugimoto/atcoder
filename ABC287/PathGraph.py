NM = list(map(int, input().split()))
V = [list(map(int, input().split()))  for i in range(NM[1])]


class UnionFind:
  def __init__(self, n):
    self.parent = list(range(n))
    self.rank = [0] * n

  def find(self, x):
    if self.parent[x] == x:
      return x
    else:
      self.parent[x] = self.find(self.parent[x])
      return self.parent[x]

  def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)

    if root_x == root_y:
      return

    if self.rank[root_x] > self.rank[root_y]:
      self.parent[root_y] = root_x
    else:
      self.parent[root_x] = root_y
      if self.rank[root_x] == self.rank[root_y]:
        self.rank[root_y] += 1

def is_connected(n, edges):
  uf = UnionFind(n)
  for edge in edges:
    uf.union(edge[0], edge[1])

  root = uf.find(0)
  for i in range(1, n):
    if uf.find(i) != root:
      return 0
  return 1

print(V)
conn = is_connected(NM[0], V)



# print(V)
p =  [0 for i in range(NM[0])]

for v in V:
  p[v[0] - 1] += 1
  p[v[1] - 1] += 1

# print(NM[0], NM[1], p)

if (conn == 0 and NM[0] - 1 == NM[1] and p.count(1) == 2 and p.count(2) == NM[0] - 2):
  print("Yes")
else:
  print("No")
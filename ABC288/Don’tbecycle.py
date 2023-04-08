class UnionFind:
  def __init__(self, n):
    self.n = n
    self.parent = list(range(n))
    self.rank = [0] * n

  def find(self, x):
    if self.parent[x] == x:
      return x
    else:
      self.parent[x] = self.find(self.parent[x])
      return self.parent[x]

  def unite(self, x, y):
    x_root = self.find(x)
    y_root = self.find(y)

    if x_root == y_root:
      return False

    if self.rank[x_root] < self.rank[y_root]:
      self.parent[x_root] = y_root
    else:
      self.parent[y_root] = x_root
      if self.rank[x_root] == self.rank[y_root]:
        self.rank[x_root] += 1

    return True

  def same(self, x, y):
    return self.find(x) == self.find(y)

n, m = map(int, input().split())
uf = UnionFind(n)
ans = 0

for _ in range(m):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  if uf.same(u, v):
    ans += 1
  uf.unite(u, v)

print(ans)

NM = list(map(int, input().split()))
V = [list(map(int, input().split()))  for i in range(NM[1])]


def find(parent, x):
    print(parent, x)
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    print("root", x_root, y_root)
    parent[x_root] = y_root

def same(parent, x, y):
    return find(parent, x) == find(parent, y)




# print(V)
parent =  [i for i in range(NM[0])]

print(parent)

for v in V:
  union(parent, v[0] - 1, v[1] - 1)

print(parent)


# for v in V:
#   p[v[0] - 1] += 1
#   p[v[1] - 1] += 1

# # print(NM[0], NM[1], p)

# if (conn == 0 and NM[0] - 1 == NM[1] and p.count(1) == 2 and p.count(2) == NM[0] - 2):
#   print("Yes")
# else:
#   print("No")
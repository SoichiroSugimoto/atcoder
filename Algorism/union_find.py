def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    parent[x_root] = y_root

def same(parent, x, y):
    return find(parent, x) == find(parent, y)

# 使用例
n = 5
parent = list(range(n))

union(parent, 1, 2)
union(parent, 3, 4)

print(same(parent, 1, 2))  # True: 1と2は同じグループに属しています
print(same(parent, 1, 3))  # False: 1と3は異なるグループに属しています

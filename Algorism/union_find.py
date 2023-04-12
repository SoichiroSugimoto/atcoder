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

# 使用例
n = 10
parent = list(range(n))

union(parent, 1, 2)
print("------------------------------")
union(parent, 5, 6)
print("------------------------------")
union(parent, 1, 5)
print(parent)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

# print(same(parent, 1, 2))  # True: 1と2は同じグループに属しています
print(same(parent, 2, 6))  # False: 1と3は異なるグループに属しています

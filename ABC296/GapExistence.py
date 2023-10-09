N, X = list(map(int, input().split()))
A = set(list(map(int, input().split())))
n = 0

for a in A:
    if (X + a in A):
        print('Yes')
        exit()
print('No')

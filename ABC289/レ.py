NM = list(map(int, input().split()))
a = list(map(int, input().split()))

p = [x for x in range(NM[0] + 1) if x > 0] 

print(NM)
print(a)
print(p)

for i in range(NM[0] + 1):
  if (p[i] == a[i]):
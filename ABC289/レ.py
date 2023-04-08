NM = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = []

i = 0
while (i < NM[0]):
  b = []
  c = a.count(i + 1)
  if (c == 0):
    ans.append([i + 1])
  while (i < NM[0] and c == 1):
    b.append(i + 1)
    i += 1
    c = a.count(i + 1)
  if (len(b) != 0):
    b.append(b[-1] + 1)
    b.reverse()
    ans.append(b)
  i += 1

ans = map(str, sum(ans, []))
print(' '.join(ans))
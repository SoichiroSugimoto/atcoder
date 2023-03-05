n = int(input())
a = list(map(int, input().split())) 

ap = 0
bp = 0

for i in range(n):
  maximum = max(a)
  if (i % 2 == 0):
    ap += maximum
  else:
    bp += maximum
  index = a.index(maximum)
  a.pop(index)

print (ap - bp)
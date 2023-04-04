NM = list(map(int, input().split()))
a = list(map(int, input().split()))

p = [x for x in range(NM[0] + 1) if x > 0] 

print(NM)
print(a)
print(p)

# for r in a:
#   tmp = p[r - 1]
#   p[r - 1] = p[r]
#   p[r] = tmp
#   print(r, p)

flg = 0
ans = []

for r in a:
  if (flg == 0):
    rsv = {}
  else:
    rsv.append(p[r - 1])
    rsv.append(p[r])
  


print(p)
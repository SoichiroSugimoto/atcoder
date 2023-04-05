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
tmp = a[0]

for i in range(len(a)):
  r = a[i]
  rsv = []
  print("----- ", r, tmp)
  while (r == tmp + 1 and i < len(a)):
    r = a[i]
    print(r, tmp, tmp + 1)
    rsv.append(p[r - 1])
    rsv.append(p[r])
    i += 1
    print(rsv)
    tmp = r
  tmp = r
  rsv.reverse()
  print(rsv)
  ans.append(rsv)

print(ans)
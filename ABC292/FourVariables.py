n = int(input())
cnt = 0
mid = 0
tmp = 0

for ab in range(n):
  cd = n - ab
  if (ab == cd):
    tmp = cnt
  if (ab > 0 and cd > 0):
    ab_cnt = 0
    cd_cnt = 0
    a = 0
    while (a * a <= ab):
      if (a > 0 and ab % a == 0):
        ab_cnt += 1
        if (ab != a * a):
          ab_cnt += 1
      a += 1
    c = 0
    while (c * c <= cd):
      if (c > 0 and cd % c == 0):
        cd_cnt += 1
        if (cd != c * c):
          cd_cnt += 1
      c += 1
    cnt += (ab_cnt * cd_cnt)
  if (ab == cd):
    mid = cnt - tmp
    break

print (tmp * 2 + mid)

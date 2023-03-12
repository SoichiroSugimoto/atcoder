n = int(input())
cnt = 0

for ab in range(n):
  cd = n - ab
  if (ab > 0 and cd > 0):
    ab_cnt = 0
    cd_cnt = 0
    for a in range(ab + 1):
      if (a > 0 and ab / a % 1 == 0):
        ab_cnt += 1
    for c in range(cd + 1):
      if (c > 0 and cd / c % 1 == 0):
        cd_cnt += 1
    cnt += (ab_cnt * cd_cnt)

print (cnt)
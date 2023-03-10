N = int(input())
p = [list(map(int, input().split()))  for i in range(N)]
p.insert(0, [0, 0, 0])

for n in range(N):
  t =  p[n + 1][0] - p[n][0]
  x =  p[n + 1][1] - p[n][1]
  y =  p[n + 1][2] - p[n][2]
  flg = 0
  for a in range(t):
    b = t - a
    if (abs(a - b) == abs(x + y)):
      flg = 1
      break
  if (flg == 0):
    print ("No")
    exit()

print ("Yes")
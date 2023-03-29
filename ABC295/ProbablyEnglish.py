n = int(input())
W = list(input().split())

comp = ['and', 'not', 'that', 'the', 'you']
flg = 0

for w in W:
  for c in comp:
    if (w == c):
      flg = 1
      break
  if (flg == 1):
    break

if (flg == 1):
  print("Yes")
else:
  print("No")
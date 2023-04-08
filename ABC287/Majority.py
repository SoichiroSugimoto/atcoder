N = int(input())
S = [list(map(str, input().split()))  for i in range(N)]

cnt = 0
for s in S:
  if (s == ["For"]):
    cnt += 1

if (cnt > N - cnt):
  print("Yes")
else:
  print("No")
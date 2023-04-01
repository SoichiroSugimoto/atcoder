NK = list(map(int, input().split()))
S = list(input())
ans = ''
cnt = 0

for s in S:
  if (cnt < NK[1] and s == 'o'):
    ans += 'o'
    cnt += 1
  else:
    ans += 'x'

print(ans)
  
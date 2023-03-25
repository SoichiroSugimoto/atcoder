N = int(input())
A = list(map(int, input().split()))

odd = []

for a in A:
  if (a % 2 == 0):
    odd.append(a)

ans = ' '.join(list(map(str, odd)))
print(ans)
NM = list(map(int, input().split()))
S = [' '.join(map(str, input().split())) for i in range(NM[0])]
T = [' '.join(map(str, input().split())) for i in range(NM[1])]

ans = []

for i in range(NM[0]):
  num = int(S[i]) % 1000
  for t in T:
    if (num == int(t)):
      ans.append(i)

ans = set(ans)
print(len(ans))
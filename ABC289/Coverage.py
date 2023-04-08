NM = list(map(int, input().split()))
S = [list(map(int, input().split()))  for i in range(NM[1] * 2)]

ans = 0

def judge(array, n):
  for i in range(n):
    if (array.count(i + 1) == 0):
      return 0
  return 1

for i in range(2**NM[1]):
  combination = []
  for j in range(NM[1]):
    if (i >> j) & 1:
      combination.append(S[2*j + 1])
  
  ans += judge(sum(combination, []), NM[0])

print(ans)
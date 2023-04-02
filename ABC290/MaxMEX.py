NK = list(map(int, input().split()))
A = list(map(int, input().split()))
flg = 0

array = list(set(A))

for i in range(NK[1]):
  if (array.count(i) == 0):
    print(i)
    flg = 1
    break
if (flg == 0):
  print(NK[1])

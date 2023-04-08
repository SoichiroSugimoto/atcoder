N = int(input())
AB = [list(map(int, input().split()))  for i in range(N)]

for num in AB:
  print(num[0] + num[1])
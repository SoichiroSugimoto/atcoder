i = input().split()
N = int(i[0])
Y = int(i[1])

for x in range(N + 1):
  for y in range(N + 1 - x):
    z = N - x - y
    if (z < 0):
      break
    if (Y == 10000 * x + 5000 * y + 1000 * z):
      print (x, y, z)
      exit()

print (-1, -1, -1)

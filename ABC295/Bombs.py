rc = list(input().split())
grid = [input() for i in range(int(rc[0]))]

i = 0
for g in grid:
  j = 0
  for c in g:
    if (['0123456789'].find(c)):
      power = int(c)
      j += 1
      tmp_i = i
      tmp_j = j
      if (abs(i) + abs(j) < c)
  i += 1
    print(c)
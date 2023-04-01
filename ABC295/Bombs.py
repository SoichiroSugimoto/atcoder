rc = list(input().split())
grid = [list(input()) for i in range(int(rc[0]))]
r = int(rc[0])
c = int(rc[1])

for i in range(r):
  for j in range(c):
    if ('0123456789'.find(grid[i][j]) > -1):
      power = int(grid[i][j])
      grid[i][j] = '.'
      for ni in range(r):
        for nj in range(c):
          if (abs(ni - i) + abs(nj - j) <= power and grid[ni][nj] == '#'):
            grid[ni][nj] = '.'

for R in grid:
  line = ''.join(R)
  print(line)
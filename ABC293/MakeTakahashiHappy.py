hw = input().split()
grid = [list(map(int, input().split()))  for i in range(int(hw[0]))]

ans = 0
height = int(hw[0])
width = int(hw[1])

def func(i, j, via):
  global ans
  while (i + j - 2 < len(via)):
    via.pop(len(via) - 1)
  if (i > height or j > width):
    return False
  via.append(grid[i-1][j-1])
  if (i == height and j == width and len(set(via)) == height + width - 1):
    ans += 1
  if (func(i+1, j, via)):
    return True
  if (func(i, j+1, via)):
    return True
  return False

func(1, 1, [])
print(ans)
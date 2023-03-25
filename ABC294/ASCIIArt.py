hw = input().split()
grid = [list(map(int, input().split()))  for i in range(int(hw[0]))]

s = []

for h in grid:
  line = ''
  for num in h:
    if (num == 0):
      line += '.'
    elif (num > 0 and num <= 26):
      line += chr(num + 64)
  s.append(line)

ans = "\n".join(s)
print(ans)
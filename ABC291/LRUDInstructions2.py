N = int(input())
S = input()
path = [[0, 0]]
p = [0, 0]
ans = "No"

for dirc in S:
  if (dirc == 'R'):
    p[0] += 1
  elif (dirc == 'L'):
    p[0] -= 1
  elif (dirc == 'U'):
    p[1] += 1
  elif (dirc == 'D'):
    p[1] -= 1
  if (p in path):
    ans = "Yes"
    break
  else:
    path.append([p[0], p[1]])

print(ans)
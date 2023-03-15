s = list(input())
len = len(s)

tmp = ''

for n in range(int(len / 2) + 1):
  if (n > 0):
    tmp = s[2 * n - 2]
    s[2 * n - 2] = s[2 * n - 1]
    s[2 * n - 1] = tmp

print (''.join(s))
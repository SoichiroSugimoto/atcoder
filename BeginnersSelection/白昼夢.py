s = input()
t = ''
flg = 0
tmp = ''

while (flg == 0):
  for word in ["dream", "dreamer", "erase", "eraser"]:
    tmp = t
    t = word + t
    if (s == t):
      print ("YES")
      exit()
    n = 0
    for i in range(len(word)):
      if (-1 * (-1 - i - len(tmp)) > len(s)):
        break
      if (word[-1 - i] == s[-1 - i - len(tmp)]):
        n += 1
    if (n == len(word)):
      break
    elif (word == "eraser"):
      flg = -1
    else:
      t = tmp
print ("NO")

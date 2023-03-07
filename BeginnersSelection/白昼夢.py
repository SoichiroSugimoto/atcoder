s = input()
t = ''

flg = 0
cnt = len(s)

while (flg == 0):
  for word in ["dream", "dreamer", "erase", "eraser"]:
    tmp_t = t
    t = word + t
    # print (t)
    if (t == s):
      print ("YES")
      exit()
    tmp_cnt = cnt
    i = 0
    # for i in range(len(word)):
    while (i < len(word)):
      # print (len(s) - 1 - cnt - i, cnt, s[len(s) - 1 - cnt - i], word[len(word) - 1 - i])
      if (s[len(s) - 1 - cnt - i] != word[len(word) - 1 - i]):
        t = tmp_t
        # print ("========")
        break
      i += 1
    if (t != tmp_t):
      # print (t)
      break
  if (t == tmp_t):
    flg = -1
  else:
    cnt += (len(t) - 2)

print ("NO")
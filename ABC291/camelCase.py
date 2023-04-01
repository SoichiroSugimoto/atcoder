s = list(input())
i = 1

for c in s:
  if (65 <= ord(c) and ord(c) <= 90):
    print(i)
    break
  i += 1

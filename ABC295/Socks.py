N = int(input())
A = list(input().split())
dic = {}
count = 0

for a in A:
  if (a in dic):
    dic[a] += 1
  else:
    dic[a] = 1

for d in dic.values():
  count += int(d / 2)

print (count)
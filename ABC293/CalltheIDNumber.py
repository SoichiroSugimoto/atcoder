n = int(input())
a = sorted(set(list(map(int, input().split()))))

x = []
i = 0

print (a)
length = len(a)

for num in range(n + 1):
  if (num > 0):
    if (a[i] != num):
      x.append(num)
    elif (length > i + 1):
      i += 1

print (len(x))
print (x)
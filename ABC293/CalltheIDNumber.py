n = int(input())
a = list(map(int, input().split()))

b = []
called = []

for num in range(n + 1):
  if (num > 0):
    b.append(int(num))
    jg = int(num) in called
    if (jg == False):
      called.append(int(a[num - 1]))
    num += 1

x = set(b) ^ set(called)
print (len(x))
x = map(str, x)
print (' '.join(x))
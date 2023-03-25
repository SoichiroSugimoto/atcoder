def func(i, x, a):
  print (i, x)
  if (i == 0):
    if (x == 0):
      return True
    else:
      return False
  if (func(i-1, x, a)):
    return True
  if (func(i-1, x-a[i-1], a)):
    return True
  return False

n = int(input())
a = list(map(int, input().split()))
x = int(input())

if (func(n, x, a)):
  print(True)
else:
  print(False)
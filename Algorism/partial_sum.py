def func(i, x, a):
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

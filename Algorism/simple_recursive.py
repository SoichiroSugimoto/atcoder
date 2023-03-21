n = int(input())

def func(n):
  if (n == 0):
    return 0
  return n + func(n - 1)

sum = func(n)

print(sum)
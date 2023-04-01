NM = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum_p = 0

for b in B:
  sum_p += A[b - 1]

print(sum_p)
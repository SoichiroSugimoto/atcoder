A, B = list(map(int, input().split()))
n = 0

HP = A % B
n = int(A // B)
while (HP > 0):
    HP -= B
    n += 1

print(n)
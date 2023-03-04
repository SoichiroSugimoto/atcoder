s = list(map(int, input().split()))
cnt = 0

for n in range(s[0]):
    num = n + 1
    sum = 0
    while num >= 1:
        sum += num % 10
        num = int(num / 10)
    if (s[1] <= sum and sum <= s[2]):
        cnt += (n + 1)
print (cnt)
n = int(input())
s = list(map(int, input().split())) 
cnt = 0
f = 0
while (1):
    for i in range(n):
        if (s[i] % 2 != 0):
            print (cnt)
            exit()
        s[i] /= 2
    cnt += 1
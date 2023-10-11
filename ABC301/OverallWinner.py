N = int(input())
S = input()

t = 0
a = 0
for i in range(N):
    if (S[i] == 'T'):
        t += 1
    else:
        a += 1
    if (t >= a + N - i - 1):
        print('T')
        exit()
    elif (a >= t + N - i - 1):
        print('A')
        exit()

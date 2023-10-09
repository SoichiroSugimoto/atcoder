N = int(input())
S = input()
g = 0
b = 0

for s in S:
    if (s == 'o'):
        g += 1
    elif (s == 'x'):
        b += 1

if (g >= 1 and b == 0):
    print('Yes')
else:
    print('No')
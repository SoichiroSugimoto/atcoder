N = int(input())
S = input()

p1 = 0
p2 = 0
o = 0
f_p = 0

for n in range(N):
    if (S[n] == '|' and f_p == 0):
        p1 = n
        f_p = 1
    elif (S[n] == '|' and f_p == 1):
        p2 = n
    elif (S[n] == '*'):
        o = n

if (p1 < o and o < p2):
    print('in')
else:
    print('out')

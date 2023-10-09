S = input()
B_flg = 0
R_flg = 0

for i in range(len(S)):
    if (S[i] == 'B' and B_flg == 0):
        B1 = i + 1
        B_flg = 1
    elif (S[i] == 'B' and B_flg == 1):
        B2 = i + 1
    elif (S[i] == 'R' and R_flg == 0):
        R1 = i + 1
        R_flg = 1
    elif (S[i] == 'R' and R_flg == 1):
        R2 = i + 1
    elif (S[i] == 'K'):
        K = i + 1

if ((B1 + B2) % 2 == 1 and R1 < K and K < R2):
    print('Yes')
else:
    print('No')

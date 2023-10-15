N = int(input())
S = input()
T = input()

for i in range(N):
    if not ((S[i] + T[i]) in ['ll', '11', '1l', 'l1', 'o0', '0o', '00', 'oo'] or S[i] == T[i]):
        print('No')
        exit()
print('Yes')
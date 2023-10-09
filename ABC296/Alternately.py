N = int(input())
S = input()

for i in range(N):
    if i == 0:
        continue
    if S[i] == S[i-1]:
        print('No')
        exit()
print('Yes')

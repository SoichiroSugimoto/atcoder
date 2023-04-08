NK = list(map(int, input().split()))
S = sum([list(map(str, input().split()))  for i in range((NK[0]))], [])

K = []

def bubble_sort(strings):
  n = len(strings)

  for i in range(n):
    for j in range(0, n - i - 1):
      if strings[j] > strings[j + 1]:
        strings[j], strings[j + 1] = strings[j + 1], strings[j]

  return strings


for i in range(NK[1]):
  K.append(S[i])

ans = "\n".join(bubble_sort(K))

print(ans)

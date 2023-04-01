N = int(input())
X = list(map(int, input().split()))
ans = []

def quick_sort(data):
  if len(data) <= 1:
    return data
  pivot = data.pop(0)
  left = [i for i in data if i <= pivot]
  right = [i for i in data if i > pivot]
  left = quick_sort(left)
  right = quick_sort(right)
  return left + [pivot] + right

X = quick_sort(X)

for i in range(len(X)):
  if (i >= N and i < len(X) - N):
    ans.append(X[i])

print (sum(ans)/len(ans))
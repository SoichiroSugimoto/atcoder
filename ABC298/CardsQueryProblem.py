N = int(input())
Q = int(input())
Query = [list(map(int, input().split()))  for i in range(Q)]

B = []
H = {}

for q in range(N):
    B.append([])

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

for q in Query:
    if (q[0] == 1):
        B[q[2] - 1].append(q[1])
        if (chr(q[1]) not in H):
            H[chr(q[1])] = [q[2]]
        elif (q[2] not in H[chr(q[1])]):
            H[chr(q[1])].append(q[2])
    elif (q[0] == 2):
        print(' '.join(map(str, quicksort(B[q[1] - 1]))))            
    elif (q[0] == 3):
        print(' '.join(map(str, quicksort(H[chr(q[1])]))))
        
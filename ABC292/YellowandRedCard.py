nq = input().split()
e = [list(map(int, input().split()))  for i in range(int(nq[1]))]
status = [0 for j in range(int(nq[0]))]


for a in e:
  if (a[0] == 1):
    status[a[1] - 1] += 1
  elif (a[0] == 2):
    status[a[1] - 1] += 2
  elif (a[0] == 3):
    if (status[a[1] - 1] >= 2):
      print ("Yes")
    else:
      print ("No")
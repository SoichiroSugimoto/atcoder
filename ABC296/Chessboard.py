row_0 = input()
height = len(row_0)
two_d_list = [list(input())  for i in range(height - 1)]
grid = [list(row_0)] + two_d_list

for i in range(height):
    for j in range(height):
        if (grid[i][j] == '*'):
            print(chr(ord('a') + j) + str(height - i))
            exit()

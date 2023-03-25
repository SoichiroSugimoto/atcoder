# string
string = input()

# integer
integer = int(input())

# str型list
str_list = list(input().split())

# int型list
int_list = list(map(int, input().split()))

# int型list(縦型入力)
height = int(input())
int_list = [int(input()) for i in range(height)]

# 二次元int型list
height = int(input())
two_d_list = [list(map(int, input().split()))  for i in range(height)]

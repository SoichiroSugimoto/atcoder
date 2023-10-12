S = list(input())
T = list(input())

s_at_cnt = S.count('@')
s_a = S.count('a')
s_t = S.count('t')
s_c = S.count('c')
s_o = S.count('o')
s_d = S.count('d')
s_e = S.count('e')
s_r = S.count('r')
s_other = len(S) - s_at_cnt - s_a - s_t - s_c - s_o - s_d - s_e - s_r
t_at_cnt = T.count('@')
t_a = T.count('a')
t_t = T.count('t')
t_c = T.count('c')
t_o = T.count('o')
t_d = T.count('d')
t_e = T.count('e')
t_r = T.count('r')
t_other = len(T) - t_at_cnt - t_a - t_t - t_c - t_o - t_d - t_e - t_r

if (s_a < t_a):
    s_at_cnt -= t_a - s_a
elif (s_a > t_a):
    t_at_cnt -= s_a - t_a
if (s_t < t_t):
    s_at_cnt -= t_t - s_t
elif (s_t > t_t):
    t_at_cnt -= s_t - t_t
if (s_c < t_c):
    s_at_cnt -= t_c - s_c
elif (s_c > t_c):
    t_at_cnt -= s_c - t_c
if (s_o < t_o):
    s_at_cnt -= t_o - s_o
elif (s_o > t_o):
    t_at_cnt -= s_o - t_o
if (s_d < t_d):
    s_at_cnt -= t_d - s_d
elif (s_d > t_d):
    t_at_cnt -= s_d - t_d
if (s_e < t_e):
    s_at_cnt -= t_e - s_e
elif (s_e > t_e):
    t_at_cnt -= s_e - t_e
if (s_r < t_r):
    s_at_cnt -= t_r - s_r
elif (s_r > t_r):
    t_at_cnt -= s_r - t_r

if (s_at_cnt == t_at_cnt):
    print('Yes')
else:
    print('No')

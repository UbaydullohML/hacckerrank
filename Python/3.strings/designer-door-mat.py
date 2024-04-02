n, m = map(int, input().split())
me = ".|."
wel = 'WELCOME'
for i in range(n//2):
    print((me*i).rjust(m//2-1,'-')+me+(me*i).ljust(m//2-1,'-'))
print(wel.center(m,'-'))
for i in range(n//2-1,-1,-1):
    print((me*i).rjust(m//2-1,'-')+me+(me*i).ljust(m//2-1,'-'))

# # 2nd option with center
# for i in range(n//2):
#     print((pa*(2*i+1)).center(m,'-'))
# print((wel).center(m,'-'))
# for i in range(n//2-1, -1, -1):
#     print((pa*(2*i+1)).center(m,'-'))

# 3 rd case
# for i in range(n//2):
#     print((me*i).rjust(m//2-1,'-')+me+(me*i).ljust(m//2-1,'-'))
# print((wel).center(m,'-'))
# for i in range(n//2):
#     print((me*(n//2-i-1)).rjust(m//2-1,'-')+me+((me*(n//2-i-1))).ljust(m//2-1,'-'))


# Task: Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
# Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
# The design should have ‘WELCOME’ written in the center.
# The design pattern should only use |, . and – characters.




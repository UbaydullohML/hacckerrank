m = int(input())
mi = set(map(int, input().split()))
n = int(input())
ni = set(map(int, input().split()))

o = mi.difference(ni)
o1 = ni.difference(mi)
for i in sorted(o.union(o1)):
    print(i)



# Sample Input
# STDIN       Function
# -----       --------
# 4           set a size M = 4
# 2 4 5 9     a = {2, 4, 5, 9}
# 4           set b size N = 4
# 2 4 11 12   b = {2, 4, 11, 12}

# Sample Output
# 5
# 9
# 11
# 12

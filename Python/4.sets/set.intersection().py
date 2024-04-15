n = input() 
ns = set(map(int, input().split())) 
b = input() 
bs = set(map(int, input().split())) 
 
output = len(ns.intersection(bs)) 
print(output)


# Task
# The first line contains n, the number of students who have subscribed to the English newspaper.
# The second line contains n space separated roll numbers of those students.
# The third line contains b, the number of students who have subscribed to the French newspaper.
# The fourth line contains b space separated roll numbers of those students.

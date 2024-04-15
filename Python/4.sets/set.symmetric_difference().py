n = input() 
ns = set(map(int, input().split())) 
b = input() 
bs = set(map(int,input().split())) 
 
output = ns.symmetric_difference(bs) 
print(len(output))


# Input Format
# The first line contains the number of students who have subscribed to the English newspaper.
# The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper.
# The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

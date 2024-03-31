# text wrap with built-in function
import textwrap
def wrap(string, max_width):
    o = textwrap.fill(string, max_width)
    return o 

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# Sample Input 0
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4

# Sample Output 0
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

# without built in 
warped = []
def wrap(string, max_width):
    for i in range(0, len(string), max_width):
        warped.append(string[i:i+max_width])
    o = warped
    o = '\n'.join(o)
    return o

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

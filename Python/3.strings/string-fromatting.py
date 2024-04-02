def print_formatted(number):
    p = (len(bin(number)))-2
    #p = len(bin(number)[1:])
    for i in range(1,number+1,1):
        #print(format(i,'d'), format(i,'o'), format(i,'X'), format(i,'b'))
        print(f"{i:{p}d} {i:{p}o} {i:{p}X} {i:{p}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# Task: Given an integer, n, print the following values for each integer i from 1 to n:
# Decimal 
# Octal 
# Hexadecimal (capitalized)
# Binary
# The four values must be printed on a single line in the order specified above for each i from 1 to n. Each value should be space-padded to match the width of the binary value of n.

def mutate_string(string, position, character):
    l = list(string)        # list(), it reads like this list of string ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']
    l[position] = character
    l1 = "".join(l)    # adding all character as abrackdabra
    return l1

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
# You are given an immutable string, and you want to make changes to it.


# Sample Input
# STDIN           Function
# -----           --------
# abracadabra     s = 'abracadabra'
# 5 k             position = 5, character = 'k'

# Sample Output
# abrackdabra

if __name__ == '__main__':
    N = int(input())
    list =[]
    for _ in range(N):
        cmd = input().split()
        if cmd[0] == 'insert':
            list.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'print':
            print(list)
        elif cmd[0] == 'remove':
            list.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            list.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            list.sort()
        elif cmd[0] == 'pop':
            list.pop()
        elif cmd[0] == 'reverse':
            list.reverse()


# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer  at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

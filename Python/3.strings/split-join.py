def split_and_join(line):
    output = line.split()  # is converted to a list of strings. as. ['This', 'is', 'a', 'test']
    output = "-".join(output)  # it joins them into single string, , separated by hyphen
    return output

if __name__ == '__main__':

#   Example:In Python, a string can be split on a delimiter.

# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings. 
# >>> print a
# ['this', 'is', 'a', 'string']
# Joining a string is simple:

# >>> a = "-".join(a)
# >>> print a
# this-is-a-string 

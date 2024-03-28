if __name__ == '__main__':
    s = input()
    print(any(str.isalnum() for str in s))
    print(any(str.isalpha() for str in s))
    print(any(str.isdigit() for str in s))
    print(any(str.islower() for str in s)) 
    print(any(str.isupper() for str in s)) 

    # 2nd option:
    # print(any(map(str.isalnum, s))) 
    # print(any(map(str.isalpha, s)))
    # print(any(map(str.isdigit, s)))
    # print(any(map(str.islower, s)))
    # print(any(map(str.isupper, s))) # map() applyies str.isalnum to every character in string s


# Task
# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

# Sample Input
# qA2

# Sample Output
# True
# True
# True
# True
# True

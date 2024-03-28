def count_substring(string, sub_string):
    count = 0
    sub_len = len(sub_string)
    for i in range(len(string)-sub_len+1): 
        if string[i:i+sub_len] == sub_string: # string[i:i+sub_len] , it slices string to [0:2]  , [1:3], [2:4], [3:5] samples if s=5,sbs=2
        # If the slice equals, we have found an occurrence 
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
# Sample Input
# ABCDCDC
# CDC

# Sample Output
# 2

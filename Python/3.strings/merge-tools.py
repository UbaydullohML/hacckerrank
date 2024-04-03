wrap = []
def merge_the_tools(string, k):
    for i in range(0, len(string),k):
        wrap = string[i:i+k]
        o = sorted(set(wrap), key=wrap.index) # sorted based on indices of charachters, key=wrap.index , it generates index key for each element
        o="".join(o) # it joins list into single string with empty string  ['f''s'] -> f s
        print(o)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# 2nd option:
# wrap = []
# def merge_the_tools(string, k):
#     for i in range(0, len(string), k):
#         wrap = string[i:i+k]
#         o = sorted(set(wrap), key=lambda x:wrap.index)
#         o = "".join(o)
#         print(o)

# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)

  
# Task: s = “AAABCADDE”
# k = 3
# There are three substrings of length 3 to consider: ‘AAA’, ‘BCA’ and ‘DDE’. The first substring is all ‘A’ characters, so u1 = ‘A’. 
# The second substring has all distinct characters, so u2 = ‘BCA’. The third substring has 2 different characters, so u3 = ‘DE’. 
# Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.

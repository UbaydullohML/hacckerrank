def minion_game(string):
    vowels = "aeiou".upper()
    stu = 0
    kev = 0
    for i in range(len(string)):
        if string[i] in vowels:   # checks current charecter is vowel
            kev +=  len(string)-i  # it adds count of remaining characters in string.
        else:
            stu += len(string)-i
            
    if stu == kev:
        print("Draw")
    elif stu > kev:
        print("Stuart", stu)
    else:
        print("Kevin", kev)

if __name__ == '__main__':
    s = input()
    minion_game(s)

# Task: Game Rules
# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.


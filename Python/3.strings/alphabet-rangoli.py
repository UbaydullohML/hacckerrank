def print_rangoli(size):
    w = (size-1)*2 + ((size*2)-1)
    for i in range(1,size):
        nl = (i*2)-1  # 1 letter (1*2-1 = 1)
        s = ""
        letter_value = 97 +n-1   # starting value 101, e (97 + 5-1)
        for i in range(nl):
            if i !=0:
                s+="-"
            s +=chr(letter_value)
            if i < (nl-1)/2:
                letter_value -= 1
            else: 
                letter_value +=1
        print(s.center(w,'-'))
    for i in range(size,0, -1):
        nl = (i*2)-1
        s=""
        letter_value = 97+n-1
        for i in range(nl):
            if i !=0:
                s+="-"
            s+=chr(letter_value)
            if i < (nl-1)/2:
                letter_value -=1
            else:
                letter_value +=1
        print(s.center(w,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

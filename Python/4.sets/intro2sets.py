def average(array):
    ar = set(array)
    o = sum(ar)/len(ar)
    return round(o,3)
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

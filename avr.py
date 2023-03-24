from operator import length_hint

def average(array):
    array=set(array)
    sum1=sum(array)
    len1=len(array)
    return sum1/len1

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
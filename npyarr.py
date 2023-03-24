import numpy

def arrays(arr):
    arr.reverse()
    return numpy.array(arr,float)
    

arr = input().split(' ')
print(arrays(arr))
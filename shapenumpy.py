import numpy

n = input().strip().split(" ") #9 input (3,3)
arr = []
for i in n:
    arr.append(int(i))

arr = numpy.array(arr)
arr= arr.reshape(3,3)
print(arr)

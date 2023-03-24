import numpy
n,m = list(map(int, input().split()))
list = []
for i in range(n):
    list.append(input().split())
list = numpy.array(list, int)
list = numpy.min(list, axis =1)
list = numpy.max(list)
print(list)
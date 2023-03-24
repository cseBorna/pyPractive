import numpy

n,m,l = list(map(int, input().split()))
list = []
for i in range(n):
    list.append(input().split())
for a in range(m):
    list.append(input().split())
list = numpy.array(list, int)
print(list)